import time

from webserver import *
import logging

from detection import apiRequest

logging.getLogger().setLevel(logging.INFO)

if __name__ == '__main__':
    #startCleanup()
    time.sleep(2)
    overrideRubbishValues([10,20,30])
    getRubbishValues()
    time.sleep(2)
    overrideRubbishValues([40,50,60])
    getRubbishValues()
    uploadImage()
    #file, predictionClass, predictionConfidence = apiRequest()

