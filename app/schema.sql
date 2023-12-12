DROP TABLE IF EXISTS question;

CREATE TABLE question (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quiz TEXT NOT NULL,
    author TEXT NOT NULL,
    title TEXT NOT NULL,
    answer1 TEXT NOT NULL,
    answer2 TEXT NOT NULL,
    answer3 TEXT NOT NULL,
    answer4 TEXT NOT NULL,
    correctAnswer INTEGER NOT NULL,
    imageUrl BLOB NOT NULL
);
