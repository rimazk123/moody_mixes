from google.cloud import vision
from google.cloud.vision import types
import io
import os

likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY')



def get_face_emotions(file):
    emotions = {}

    path = "./images/" + file
    client = vision.ImageAnnotatorClient()
    #file_name = os.path.abspath(path)

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content = content)

    response = client.face_detection(image = image)
    face = response.face_annotations

    emotions['joy'] = face[0].joy_likelihood
    emotions['anger'] = face[0].anger_likelihood
    emotions['suprise'] = face[0].surprise_likelihood
    emotions['sorrow'] = face[0].sorrow_likelihood
    

    print(emotions)
    return emotions
    
    # for face in faces:
    #     print(face.anger_likelihood)
    #     print(face.joy_likelihood)
    #     #print(anger.format(likelihood_name[face.anger_likelihood]))
    #     print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
    #     print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
    #     print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
    #     print('sorrow: {}' .format(likelihood_name[face.sorrow_likelihood]))



# response = client.face_detection({
#    'source': {'image_uri': 'https://www.incimages.com/uploaded_files/image/970x450/laugh1_24055.jpg'},
# })

# with io.open('./images/laugh1_24055.jpg', 'rb') as image_file:
#     content = base64.b64encode(image_file.read())

#image = vision.types.Image(content = content)

#response = client.image_properties(image=image)
# print(response)

# props = response.face_annotations
# print('Properties of the image:')

# for color in props.dominant_colors.colors:
#     print('Fraction: {}'.format(color.pixel_fraction))
#     print('\tr: {}'.format(color.color.red))
#     print('\tg: {}'.format(color.color.green))
#     print('\tb: {}'.format(color.color.blue))

# file_name = os.path.abspath('./images/MM95820ab7d32ee281bff8f8b9af213f85.png')

# with io.open(file_name, 'rb') as image_file:
#     content = image_file.read()

# image = types.Image(content = content)





# response = client.face_detection(image = image)
# print(response)

# faces = response.face_annotations

# likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
#                        'LIKELY', 'VERY_LIKELY')


# faces = response.face_annotations

# for face in faces:
#         print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
#         print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
#         print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

#         # vertices = (['({},{})'.format(vertex.x, vertex.y)
#         #             for vertex in face.bounding_poly.vertices])

        # print('face bounds: {}'.format(','.join(vertices)))
