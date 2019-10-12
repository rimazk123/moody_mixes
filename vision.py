from google.cloud import vision
from google.cloud.vision import types
import base64
import io
import os


client = vision.ImageAnnotatorClient()

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

file_name = os.path.abspath('happy.png')

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content = content)





response = client.face_detection(image = image)
print(response)

faces = response.face_annotations

likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')


faces = response.face_annotations

for face in faces:
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

        # vertices = (['({},{})'.format(vertex.x, vertex.y)
        #             for vertex in face.bounding_poly.vertices])

        # print('face bounds: {}'.format(','.join(vertices)))
