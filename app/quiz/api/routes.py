from quiz.api import api

from flask import request, Blueprint

api_blueprint = Blueprint('api', __name__)

"""
API endpoint for quiz

- GET will return list of questions for quiz
- POST will do grading
"""
@api_blueprint.route('/quizzes/<quiz_name>', methods=['GET', 'POST'])
def quiz_methods(quiz_name):
    if request.method == 'GET':
        return api.get_questions(quiz_name)
    elif request.method == 'POST':
        answers = request.get_json()
        return api.get_grade(quiz_name, answers)
    else:
        return "The Quiz API only supports GET and POST requests"

"""
API endpoint for feedback
"""
@api_blueprint.route('/quizzes/feedback/<quiz_name>', methods=['POST'])
def feedback_method(quiz_name):
    feedback = request.get_json()
    return

"""
API endpoint for liveness
"""
@api_blueprint.route('/healthz/liveness', methods=['GET'])
def liveness_method():
    api.liveness()
    return

"""
API endpoint for readiness
"""
@api_blueprint.route('/healthz/readiness', methods=['GET'])
def readiness_method():
    api.readiness()
    return
