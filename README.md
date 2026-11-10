# RoadHawk

RoadHawk finds potholes and reports where they are. A Raspberry Pi in the vehicle carries three sensors and a camera, a CNN detects potholes, and the driver gets an alert. Each detection goes to a Django backend with its GPS position, and road authorities sign in to a dashboard that lists every reported pothole with a link to its location on Google Maps.

RoadHawk made the CiiA Top 80 in India, out of 695 teams, in both 2024 and 2025.

**Demo video:** [watch on Google Drive](https://drive.google.com/file/d/14mTErMcbRGTTpAV6_aSqs2bI6zx26nnG/view)

## What's in this repository

This repo holds the server side: the endpoint the device posts to, plus the authorities' dashboard. The Raspberry Pi code and the CNN are not included here.

## How it works

```
Raspberry Pi (sensors + camera, CNN)
        │  JSON POST: ultrasonic, gyroscope x/y/z, GPS lat/long
        ▼
Django app  ──►  SQLite (one potData row per pothole)
        │
        ▼
/home dashboard (sign-in required): a card per pothole with its readings
and a Google Maps link to its coordinates
```

1. When the device detects a pothole, it sends a JSON `POST` to `/` with the ultrasonic distance (`ultra`), the gyroscope readings (`gyro_x`, `gyro_y`, `gyro_z`) and the GPS position (`gps_lat`, `gps_long`).
2. `app1/views.py` (`index`) stores each report as a `potData` row (`app1/models.py`).
3. Authorities sign up and sign in through Django's built-in auth (`/signup`, `/signin`). The dashboard at `/home` lists every stored pothole, and each location links to `https://www.google.com/maps?q=<lat>,<long>`.
4. The Django admin at `/admin/` is branded "RoadHawk Admin" for managing users and records.

## Stack

- **Device:** Raspberry Pi, three sensors and a camera, CNN-based pothole detection
- **Backend:** Python, Django 4.2, SQLite
- **Frontend:** Django templates, Bootstrap, Google Maps links

## Run the backend locally

There is no `requirements.txt`; Django is the only dependency.

```bash
python -m venv .venv && source .venv/bin/activate
pip install "django>=4.2,<5"
python manage.py migrate
python manage.py createsuperuser        # optional, for /admin/
python manage.py runserver 0.0.0.0:8000
```

Open http://127.0.0.1:8000. To accept reports from a device on your network, add the server's LAN IP to `ALLOWED_HOSTS` in `project1/settings.py`.

To post a test report the way the device does (the values below are only an example):

```bash
curl -X POST http://127.0.0.1:8000/ \
  -H "Content-Type: application/json" \
  -d '{"ultra": 12.5, "gyro_x": 0.4, "gyro_y": -1.2, "gyro_z": 9.6, "gps_lat": 19.0760, "gps_long": 72.8777}'
```

Then sign in and open `/home` to see it.

## Project structure

```
project1/        Django project settings and root URLs
app1/            potData model, ingest endpoint, auth views, dashboard view
templates/       landing page, sign-in/sign-up pages, dashboard
static/          CSS and images
```
