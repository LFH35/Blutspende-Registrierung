# Python standard libraries
import os
import json
import re

import requests
import urllib.parse
from datetime import date

# Third-party libraries
from flask import Flask, redirect, request, render_template, jsonify, url_for, make_response, abort
from flask_cors import CORS
from oauthlib.oauth2 import WebApplicationClient
from dotenv import load_dotenv

# Internal imports
from doner import Doner
from appointment import Appointment
from utils import new_uid, check_doner, get_iserv_provider_cfg, send_confirmation_email, authenticate_api_key

load_dotenv()

# Configuration
ISERV_CLIENT_ID = os.getenv("ISERV_CLIENT_ID")
ISERV_CLIENT_SECRET = os.getenv("ISERV_CLIENT_SECRET")
ISERV_DISCOVERY_URL = os.getenv("ISERV_DISCORVERY_URL")
TEMPLATES_AUTO_RELOAD = True

# Flask app setup
app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv("SECRET_KEY") or os.urandom(24)

# OAuth client setup
client = WebApplicationClient(ISERV_CLIENT_ID)


# Index route which is the first route the users see
@app.route("/", methods=['POST'])
def index():
    return 200


@app.route('/login', methods=['POST'])
def login():
    # Formats the URL Encoded Form Data into JSON
    data = request.form.to_dict(urllib.parse.unquote(request.get_data().decode()))
    users_name = data["name"][0]
    users_email = data["email"][0]
    unique_id = check_doner(users_email)
    if not unique_id:
        unique_id = new_uid()

    # Add User to the database
    if not Doner.get(unique_id):
        Doner.create(unique_id, users_name, users_email)

    response = make_response(redirect(os.getenv("FRONTENT_DOMAIN") + "/" + unique_id + "/questions?id=" + unique_id))
    response.set_cookie('user_id', unique_id, httponly=False)
    # Send the UserID to the frontend
    return response


@app.route("/iservlogin")
def iservlogin():
    # Find out what URL to hit for iserv login
    iserv_provider_cfg = get_iserv_provider_cfg()
    authorization_endpoint = iserv_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for iserv login and provide scopes that let you
    # retrieve user's profile from iserv
    return redirect(client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=os.getenv("API_DOMAIN") + "/iservlogin/callback",
        scope=["openid", "email", "profile"],
    ))


@app.route("/iservlogin/callback")
def callback():
    # Get authorization code iserv sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for things on behalf of a user
    iserv_provider_cfg = get_iserv_provider_cfg()
    token_endpoint = iserv_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(ISERV_CLIENT_ID, ISERV_CLIENT_SECRET),
    )

    # Parse the tokens
    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = iserv_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    unique_id = userinfo_response.json()["sub"]
    users_email = userinfo_response.json()["email"]
    users_name = userinfo_response.json()["name"]

    # User doesn't exist? Add it to the database.
    if not Doner.get(unique_id):
        Doner.create(unique_id, users_name, users_email)

    # Send user back to homepage
    return redirect(url_for("processing", unique_id=unique_id))


@app.route("/processing")
def processing():
    unique_id = request.args['unique_id']
    return redirect(os.getenv("FRONTENT_DOMAIN") + "/" + unique_id + "/questions?id=" + unique_id)


@app.route("/appointments")
def appointments():
    # GET the nearest date on today
    Appointment.add_appointment("2008-06-02")
    Appointment.add_appointment("2024-03-24")
    Appointment.add_appointment("2024-05-18")
    today = date.today()
    old_dates = Appointment.get_dates()
    new_dates = []
    nearest_date = None
    for appointment in old_dates:
        day = int(appointment.split("-")[2])
        month = int(appointment.split("-")[1])
        year = int(appointment.split("-")[0])
        new_dates.append(date(year, month, day))

    new_dates.sort()

    for appointment in new_dates:
        if appointment > today:
            nearest_date = str(appointment)
            break

        if appointment < today:
            new_dates.remove(appointment)

    # Create Appointment times
    time = 1000
    slots = [f"{day}.{month}.{year}"]

    while time <= 1500:
        slots.append([f"{str(time)[:2]}:{str(time)[2:]}", Appointment.free_slots(nearest_date, time)])
        if str(time).endswith("45"):
            time += 55
        else:
            time += 15

    return slots


@app.route("/set_appointment", methods=["POST"])
def set_appointment():
    # if request.base_url == f"{os.getenv('API_DOMAIN')}/login":  # TODO Setup API Key Access
    # Formats the URL Encoded Form Data into JSON
    data = urllib.parse.unquote(request.get_data().decode())
    json_data = json.loads(data)
    time = json_data["time"]
    appointment_date = json_data["date"]
    user_id = json_data["user_id"]

    # Format the date
    dates = appointment_date.split(".")
    for i in range(len(dates)):
        if len(dates[i]) <= 1:
            dates[i] = "0" + dates[i]

    appointment_date = f"{dates[2]}-{dates[1]}-{dates[0]}"
    mail_date = f"{dates[0]}.{dates[1]}.{dates[2]}"
    time = re.sub("\D", "", time)

    appointment_check = Doner.get(user_id).appointment
    if not appointment_check:
        Appointment.add_doner(appointment_date, int(time), user_id)
        send_confirmation_email(Doner.get(user_id), mail_date, time)

    return redirect(os.getenv("FRONTENT_DOMAIN") + "/" + user_id + "/success")

    # else:
    #     return redirect("https://giybf.com")


@app.route("/admin")
def admin():
    if current_user.is_authenticated and current_user.admin:
        Appointment.add_appointment("18-11-2023")
        # first get the date of the last registration time
        # then get from this date all appointments
        data = Appointment.get_appointment(Appointment.get_dates()[-1])
        return render_template("admin.html", data=data, doner=Doner.get)

    else:
        return redirect(url_for("index"))


@app.route("/admin/termine")
def admin_appointments():
    if current_user.is_authenticated and current_user.admin:
        Appointment.add_appointment("18-11-2023")
        # first get the date of the last registration time
        # then get from this date all appointments
        data = Appointment.get_appointment(Appointment.get_dates()[-1])
        return render_template("admin_doner_overview.html", data=data, doner=Doner.get, print=print)

    else:
        return redirect(url_for("index"))


@app.route("/admin/spender")
def admin_doners():
    if current_user.is_authenticated and current_user.admin:
        data = Appointment.get_appointment(Appointment.get_dates()[-1])
        return render_template("admin_doner_overview.html", data=data, print=print)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, use_reloader=True, debug=True, ssl_context="adhoc")
