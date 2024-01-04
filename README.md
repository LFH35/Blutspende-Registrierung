# Blutspende-Registrierung
Simple register service for Blood Donations.

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
```shell
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:5000 app:app
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

