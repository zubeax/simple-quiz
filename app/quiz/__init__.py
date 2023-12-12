"""
Setup flask
"""
from flask import Flask
from flask_healthz import healthz

app = Flask(__name__, static_folder='static')

"""
Register blueprints for api and quiz
"""
from quiz.api.routes import api_blueprint
from quiz.webapp.routes import webapp_blueprint

app.register_blueprint(api.routes.api_blueprint, url_prefix='/api')
app.register_blueprint(webapp.routes.webapp_blueprint, url_prefix='')
app.register_blueprint(healthz, url_prefix="/healthz")

app.config.update(
    HEALTHZ = {
        "live": "quiz.api.api.liveness",
        "ready": "quiz.api.api.readiness",
    }
)