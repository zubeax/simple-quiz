import json

from flask import Response
from flask_healthz import HealthError
from flask_healthz import healthz

from quiz.store import datastore

"""
Gets list of questions from datastore
- Create query
- Filter on quiz
- Call the datastore helper to get back JSON
- Pretty print JSON
- Set header and return the response
"""
def get_questions(quiz_name):
    questions = datastore.list_entities(quiz_name)
    payload = {'questions': list(questions)}
    payload = json.dumps(payload, indent=2, sort_keys=True)
    response = Response(payload)
    response.headers['Content-Type'] = 'application/json'
    return response

"""
Grades submitted answers
- Get list of questions with correct answers from datastore
- Iterate through questions, find any submitted answers that match
- Count total number of questions for which there is >0 correct answers
- Compose and pretty print payload
- Compose and return response
"""
def get_grade(quiz_name, answers):
    questions = datastore.list_entities(quiz_name, False)
#    score = len(list(filter(lambda x: x > 0,
#                    list(map(lambda q:
#                         len(list(filter(lambda answer:
#                            answer['id'] == q['id'] and
#                            int(answer['answer']) == q['correctAnswer'],
#                            answers)))
#                         , questions))
#                )))
    score = 0
    for q in questions:
        for a in answers:
            if 'id' in a:
                if a['id'] == q['id'] and int(a['answer']) == q['correctAnswer']:
                    score += 1

    payload = {'correct': score, 'total': len(questions)}
    payload = json.dumps(payload, indent=2, sort_keys=True)
    response = Response(payload)
    response.headers['Content-Type'] = 'application/json'
    return response

"""
Actuator Endpoints
"""

def printok():
    print('{"Status": "UP"}')

def liveness():
    try:
        printok()
    except Exception:
        raise HealthError("Liveness Error")

def readiness():
    try:
        printok()
    except Exception:
        raise HealthError("Readiness Error")
