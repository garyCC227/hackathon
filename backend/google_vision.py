import io
import os
import json
import glob

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.protobuf.json_format import MessageToDict

def getJson(img):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # Loads the image into memory
    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    res = MessageToDict(response)
    return res
