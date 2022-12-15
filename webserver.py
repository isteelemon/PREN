import logging
import requests

WEBSERVERURL = "http://prenh22-mdespeau.el.eee.intern/Rubbish/"

def startCleanup():
    url = WEBSERVERURL + "StartCleanup"
    resp = requests.post(url)
    logging.info("----------------------startCleanup()------------------------")
    logging.info(f"startCleanup() Serverresponse was: {resp}")
    logging.info("------------------------------------------------------------")



def overrideRubbishValues(rubbishValues):
    cigarettes = rubbishValues[0]
    petcaps = rubbishValues[1]
    beercaps = rubbishValues[2]
    parameter = f"Cigarettes={cigarettes}&Petcaps={petcaps}&BeerCaps={beercaps}"
    logging.info(f"Values sent to server: {parameter}")
    url = WEBSERVERURL + "OverrideRubbishValues?" + parameter

    resp = requests.post(url)
    logging.info("----------------------updateValues()------------------------")
    logging.info(f"updateValues() Serverresponse was: {resp}")
    logging.info("------------------------------------------------------------")



def getRubbishValues():
    url = WEBSERVERURL + "GetRubbishValues"
    resp = requests.get(url)
    logging.info("----------------------getRubbishValues()------------------------")
    logging.info(f"getRubbishValues() Serverresponse was: {resp}")
    logging.info(f"Values recieved from server: {resp.text}")
    logging.info("----------------------------------------------------------------")
    return resp.text

def uploadImage():
    file = open("test.jpg", "rb")
    name = file.name
    contentType = "jpg"
    data = file
    parameter = f"Name={name}&ContentType={contentType}&Data={data}"
    url = WEBSERVERURL + "OverrideRubbishValues?" + parameter
    resp = requests.post(url)
    logging.info("----------------------uploadImage()------------------------")
    logging.info(f"uploadImage() Serverresponse was: {resp}")
    logging.info(f"Values recieved from server: {getRubbishValues()}")
    logging.info("-----------------------------------------------------------")

def endCleanup():
    url = WEBSERVERURL + "EndCleanup"
    resp = requests.post(url)
    logging.info("----------------------endCleanup()------------------------")
    logging.info(f"endCleanup() Serverresponse was: {resp}")
    logging.info("----------------------------------------------------------")
