from common.config import ALERTS
from common.logs import CONTROLLER as logger

from flask import Flask, request
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app

from .actions import trigger_action

# Start Flask app
app = Flask(__name__)
app.logger = logger
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

# @app.before_request
# def log_request_info():
#     app.logger.debug('Headers: %s', request.headers)
#     app.logger.debug('Body: %s', request.get_data())

@app.route('/')
def index():
    app.logger.info('Call to root / path')
    return 'GrowBox420Operator'

@app.route('/alerts', methods=['GET', 'POST'])
def alerts():
    if request.method == 'POST':
        data = request.json
        status = data['status']
        for alert in data['alerts']:
            status = alert['status']
            name = alert['labels']['alertname']
            severity = alert['labels']['severity']
            ALERTS[name] += 1
            app.logger.info('Received %s: %s with severity %s', status, name, severity)
            trigger_action(status, name)
    return ALERTS