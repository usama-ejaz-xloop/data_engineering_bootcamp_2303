import os
import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn=os.environ["SENTRY_DSN"],
    integrations=[
        FlaskIntegration(),
    ],
    traces_sample_rate=1.0,
)

app = Flask(__name__)


@app.route("/test-sentry")
def trigger_error():
    division_by_zero = 1 / 0


if __name__ == "__main__":
    app.run()
