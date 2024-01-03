# Blutspende-Registrierung
Simple register service for Blood Donations

## How to start
### Frontend
cd frontend
    npm install
    npm install @sveltejs/adapter-cloudflare
    npm install -D sass
    npm run dev

### API
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:5000 app:app