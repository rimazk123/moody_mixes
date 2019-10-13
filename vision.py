from google.cloud import vision
from google.cloud.vision import types
import io
import os

likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY')



def get_face_emotions(content):
    emotions = {
        'joy': 0,
        'anger': 0,
        'surprise': 0,
        'sorrow': 0
    }

    # path = "./images/" + fileName
    client = vision.ImageAnnotatorClient()

    # with io.open(path, 'rb') as image_file:
    #     content = image_file.read()

    image = types.Image(content = content)

    response = client.face_detection(image = image)
    faces = response.face_annotations

    for face in faces:
        emotions['joy'] += face.joy_likelihood
        emotions['anger'] += face.anger_likelihood
        emotions['surprise'] += face.surprise_likelihood
        emotions['sorrow'] += face.sorrow_likelihood
    
    #print(emotions)

    # delete image after we use it.
    #os.remove(path)
    print(emotions)

    return emotions
