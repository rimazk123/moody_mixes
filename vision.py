from google.cloud import vision
from google.cloud.vision import types
import io
import os

likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY')



def get_face_emotions(fileName):
    emotions = {}

    path = "./images/" + fileName
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content = content)

    response = client.face_detection(image = image)
    face = response.face_annotations

    emotions['joy'] = face[0].joy_likelihood
    emotions['anger'] = face[0].anger_likelihood
    emotions['suprise'] = face[0].surprise_likelihood
    emotions['sorrow'] = face[0].sorrow_likelihood
    

    #print(emotions)

    # delete image after we use it.
    os.remove(path)

    return emotions