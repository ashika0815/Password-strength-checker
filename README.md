# PassGuard — Password Strength Checker

## Run
1. `python -m venv .venv`
2. Activate the virtual environment.
3. `pip install -r requirements.txt`
4. `python app.py`
5. Open `http://127.0.0.1:5000`

The API endpoint is `POST /api/check` with JSON `{ "password": "..." }`.

For production, use HTTPS, do not log passwords, and avoid storing submitted passwords. Client-side checks are for UX; server-side checks are the authoritative implementation.
