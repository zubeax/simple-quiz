from quiz.store import datastore

"""
Persists initial questions into datastore
"""
def main():

    """
    Create an array of dicts defining questions
    """
    questions = [
        {
            'quiz': u'gcp',
            'author': u'Nigel',
            'title': u'Which company runs GCP?',
            'answer1': u'Amazon',
            'answer2': u'Google',
            'answer3': u'IBM',
            'answer4': u'Microsoft',
            'correctAnswer': 2,
            'imageUrl': u''
        },
        {
            'quiz': u'gcp',
            'author': u'Nigel',
            'title': u'Which GCP product is NoSQL?',
            'answer1': u'Compute Engine',
            'answer2': u'Datastore',
            'answer3': u'Spanner',
            'answer4': u'BigQuery',
            'correctAnswer': 2,
            'imageUrl': u''
        },
        {
            'quiz': u'gcp',
            'author': u'Nigel',
            'title': u'Which GCP product is an Object Store?',
            'answer1': u'Cloud Storage',
            'answer2': u'Datastore',
            'answer3': u'Big Table',
            'answer4': u'All of the above',
            'correctAnswer': 1,
            'imageUrl': u''
        },
        {
            'quiz': u'places',
            'author': u'Nigel',
            'title': u'What is the capital of France?',
            'answer1': u'Berlin',
            'answer2': u'London',
            'answer3': u'Paris',
            'answer4': u'Stockholm',
            'correctAnswer': 3,
            'imageUrl': u''
        },
    ]

    """
    Create and persist and entity for each question
    """
    for q_info in questions:
        datastore.save_question(q_info)

if __name__ == '__main__':
    main()
