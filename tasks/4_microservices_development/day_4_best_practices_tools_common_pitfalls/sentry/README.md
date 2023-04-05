This directory contains an example application that reports errors to Sentry.

To run, use:

```
python3 -m virtualenv venv
. venv/bin/activate
pip install sentry-sdk[flask]==1.10.1 flask==2.2.2

SENTRY_DSN=... python app.py
```
