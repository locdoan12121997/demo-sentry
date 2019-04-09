import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask import Flask, render_template, abort, flash

sentry_sdk.init(
    dsn="https://8d6b43efa6eb4a72a9defce3fc4581c4@sentry.io/1434627",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/403")
def do_403():
    # flash("Wao, are you trying to hack me?")
    abort(403)


@app.route("/404")
def do_404():
    # flash("Weird, you've reached nothingness")
    abort(404)


@app.route("/500")
def do_500():
    # flash("You've just killed the server")
    abort(500)


@app.errorhandler(403)
def forbidden_error(error):
    sentry_sdk.capture_exception(error)
    return render_template('index.html')


@app.errorhandler(404)
def not_found_error(error):
    sentry_sdk.capture_exception(error)
    return render_template('index.html')


@app.errorhandler(500)
def internal_error(error):
    sentry_sdk.capture_exception(error)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
