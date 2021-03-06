import io
import os
from google.cloud import vision
from google.cloud.vision import types

class LabelImage:
    def __init__(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "files/recaptcha-236620-e131aa8f2ea1.json"

    def detect_labels(self, image_path):
        client = vision.ImageAnnotatorClient()

        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.label_detection(image=image)
        annotations = response.label_annotations
        labels = []
        for label in annotations:
            labels.append(label.description.lower())
        return labels
