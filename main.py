import os
from roboflow import Roboflow

PATH = 'C:\\Users\\finnm\\Desktop\\Testfiles\\'

if __name__ == '__main__':
    rf = Roboflow(api_key="C8CCnj3TqSWY6LzDVa1Q")
    project = rf.workspace().project("valuables-detection")
    model = project.version(1).model

    directory = os.listdir(PATH)
    testfiles = []
    for file in directory:
        testfiles.append(file)

    print(f"Testfiles available {len(testfiles)}")
    for file in testfiles:
        print(f"\n------------------------------------------\n")
        print(f"Testing model with file: {file}")
        # infer on a local image
        prediction = model.predict(PATH+file).json()
        predictionClass = prediction['predictions'][0]['predicted_classes'][0]
        predictionConfidence = prediction['predictions'][0]['predictions'][predictionClass]['confidence']

        print(f"Identified {predictionClass} with Confidence: {round(predictionConfidence,2) * 100}%")






    # save an image annotated with your predictions
    #keypredict.save(output_path=PREDICTIONPATH + f"prediction_key{i}.jpg")
    #ringpredict.save(output_path=PREDICTIONPATH + f"prediction_ring{i}.jpg")
