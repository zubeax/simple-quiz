from quiz.store import datastore

"""
upload image file into string and attach to question
- call datastore helper method to save question
"""
def save_question(data, image_file):
    if image_file:
        data['imageUrl'] = str(image_file.read())
    else:
        data['imageUrl'] = u''
    data['correctAnswer'] = int(data['correctAnswer'])
    datastore.save_question(data)
    return
