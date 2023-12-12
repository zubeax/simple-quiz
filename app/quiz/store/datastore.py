import sqlite3
from werkzeug.exceptions import abort

"""
Define a row factory that will ensure the
result set is a dict not a sqlite3 row.
"""
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_db_connection():
    conn = sqlite3.connect('database.db')
#    conn.row_factory = sqlite3.Row
    conn.row_factory = dict_factory
    return conn

def get_question(quiz):
    conn = get_db_connection()
    question = conn.execute('SELECT * FROM question WHERE quiz = ?', (quiz)).fetchone()
    conn.close()
    if question is None:
        abort(404)
    return question

"""
Returns a list of question entities for a given quiz
- filter by quiz name, defaulting to gcp
- no paging
- add in the entity key as the id property 
- if redact is true, remove the correctAnswer property from each entity
"""
def list_entities(quiz='gcp', redact=True):
    conn = get_db_connection()
    results = conn.execute('SELECT * FROM question WHERE quiz = ?',(quiz,)).fetchall()
    conn.close()

#    for result in results:
#        del result['id']

    if redact:
        for result in results:
            del result['correctAnswer']
    return results

"""
Create and persist and entity for each question
"""
def save_question(question):
#    q_entity = []
#    for q_prop, q_val in question.items():
#        q_entity[q_prop] = q_val

    q_entity = question

    conn = get_db_connection()
    conn.execute('INSERT INTO question ( quiz, author, title, answer1, answer2, answer3, answer4, correctAnswer, imageUrl ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (   q_entity['quiz'],
                    q_entity['author'],
                    q_entity['title'],
                    q_entity['answer1'],
                    q_entity['answer2'],
                    q_entity['answer3'],
                    q_entity['answer4'],
                    q_entity['correctAnswer'],
                    q_entity['imageUrl'])
                )
    conn.commit()
    conn.close()
