import os

from PIL import Image
from roboflow import Roboflow


# function expects picture name and picture location as parameters,
# picture_location refers to the path within the Raspy OS
def apiRequest(picture_name,picture_location):
    rf = Roboflow(api_key="C8CCnj3TqSWY6LzDVa1Q")
    project = rf.workspace().project("valuables-detection")
    model = project.version(1).model

    file = open("test.jpg", "rb")


    print(f"Testing model with file: {file}")
    # infer on a local image
    prediction = model.predict("C:\\Users\\finnm\\PycharmProjects\\PREN\\test.jpg").json()
    predictionClass = prediction['predictions'][0]['predicted_classes'][0]
    predictionConfidence = prediction['predictions'][0]['predictions'][predictionClass]['confidence']

    print(f"Identified {predictionClass} with Confidence: {round(predictionConfidence, 2) * 100}%")

    if(predictionConfidence >= 0.5):
        return file, predictionClass,predictionConfidence

    return 0