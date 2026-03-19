# Sizer - Project Context

## Stack
- Python 3 / Flask 3.1 / Gunicorn 23
- Deployed via Heroku (see Procfile)

## Key Files
- `app.py` — entire application (single file)
- `requirements.txt` — pip dependencies
- `Procfile` — Heroku process definition

## Common Commands
- `python app.py` — run dev server on port 5000
- `gunicorn app:app` — run production server
- `pip install -r requirements.txt` — install dependencies

## Endpoints
- `GET /` — health check
- `POST /dimensions` — accepts `{"image": "<base64>"}`, returns random dimensions

## Notes
- This is a demo/example project, not used in production
- The dimensions returned are random — there is no real image processing
- `decode_image()` validates base64 encoding but doesn't process the image
