# Blutspende-Registrierung
Simple register service for blood donations.

# How to start
## Frontend
```shell
cd frontend
```
```shell
npm install
npm install @sveltejs/adapter-cloudflare
npm install -D sass
npm run dev
```

## API
### Linux
```shell
pip install -r requirements.txt
gunicorn --keyfile ./frontend/cert/key.pem --certfile ./frontend/cert/cert.pem -b 127.0.0.1:5000 app:app
```

### Windows (Only for testing use. Do NOT use this in production!)
```shell
pip install -r requirements.txt
python3 app.py
```

## For local testing
### Install Cert for the Svelte App
1. #### Install [mkcert](https://github.com/FiloSottile/mkcert)
2. #### Install a local certificate authority
```shell
mkcert -install
```
3. #### Create your certificate with `mkcert`
```shell
cd frontend/cert
mkcert -key-file key.pem -cert-file cert.pem localhost
```


# Notes
## Datenbank
- The dates in the DB is only saved with the following format: `YYYY-MM-DD`