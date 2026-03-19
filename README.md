# Sizer

A simple Python REST API that accepts a base64-encoded image and returns random dimensions (height, length, weight). Built as a demo/example project.

## Tech Stack

- Python 3
- Flask 3.1
- Gunicorn 23

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running

Development server:

```bash
python app.py
```

Production (Gunicorn):

```bash
gunicorn app:app
```

## API

### `GET /`

Health check. Returns `{"ok": true}`.

### `POST /dimensions`

Accepts a JSON body with a base64-encoded `image` field. Returns random dimensions.

```bash
curl -X POST http://localhost:5000/dimensions \
  -H "Content-Type: application/json" \
  -d '{"image": "aGVsbG8="}'
```

Response:

```json
{
  "height": 4.23,
  "length": 12.87,
  "weight": 7.51
}
```
