import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

#cur = connection.cursor()
#
#cur.execute("INSERT INTO question ( quiz, author, title, answer1, answer2, answer3, answer4, correctAnswer, imageUrl ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
#            (   'gcp',
#                'Nigel',
#                'Which company runs GCP?',
#                'Amazon',
#                'Google',
#                'IBM',
#                'Microsoft',
#                2,
#                '')
#            )

connection.commit()
connection.close()
