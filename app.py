# Python standard libraries
import os
import json
import requests
import urllib.parse

# Third-party libraries
from flask import Flask, redirect, request, render_template, jsonify
from oauthlib.oauth2 import WebApplicationClient
from dotenv import load_dotenv

# Internal imports
from doner import Doner
from appointment import Appointment
from utils import new_uid, check_doner, get_iserv_provider_cfg

load_dotenv()

# Configuration
ISERV_CLIENT_ID = os.getenv("ISERV_CLIENT_ID")
ISERV_CLIENT_SECRET = os.getenv("ISERV_CLIENT_SECRET")
ISERV_DISCOVERY_URL = os.getenv("ISERV_DISCORVERY_URL")
TEMPLATES_AUTO_RELOAD = True

# Flask app setup
app = Flask(__name__)
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

    # Send the UserID to the frontend
    return redirect(os.getenv("FRONTENT_DOMAIN") + "/" + unique_id + "/questions")


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
    return redirect(os.getenv("FRONTENT_DOMAIN") + unique_id + "/questions")


@app.route("/logout")
def logout():
    return redirect(request.base_url)


@app.route("/questions")
def questions():
    if current_user.is_authenticated:
        return render_template("questions.html", current_user=current_user)

    else:
        return redirect(url_for("index"))


@app.route("/checkdonator", methods=['GET', 'POST'])
def checkdonator():
    if current_user.is_authenticated:
        adult: bool = bool(request.form.get('adult'))
        weight: bool = bool(request.form.get('weight'))
        healthy: bool = bool(request.form.get('healthy'))
        tattoos: bool = not bool(request.form.get('tattoos'))

        # checks if the blood is donatable
        values = [adult, weight, healthy, tattoos]
        not_donatable = []

        for value in values:
            if not value:
                not_donatable.append(value)

        if not_donatable:
            return redirect(request.base_url + "/not_donatable")

        else:
            return redirect(url_for("appointments"))

    else:
        return redirect(url_for("index"))


@app.route("/appointments")
def appointments():
    if current_user.is_authenticated:
        # REMOVE WHEN ADMIN PANEL IS ACTIVE
        Appointment.add_appointment("18-09-2023")
        return render_template("appointments.html",
                               appointments=Appointment.get_appointment("18-09-2023"),
                               free_slots=Appointment.free_slots)

    else:
        return redirect(url_for("index"))


@app.route("/set_appointment", methods=["GET", "POST"])
def set_appointment():
    if current_user.is_authenticated:
        appointment_check = current_user.appointment
        time = request.args.get('time'),
        date = Appointment.get_dates()[0]
        Appointment.add_doner(date, time[0], current_user.user_id)
        if not appointment_check:
            utils.send_confirmation_email(current_user, date, time[0])
        return render_template("confirmation.html", time_slot=time[0], date=date,
                               current_user=current_user)

    else:
        return redirect(url_for("index"))


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
    app.run(host="0.0.0.0", port=5000, use_reloader=True, debug=True, ssl_context="adhoc")
