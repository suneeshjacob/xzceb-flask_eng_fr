import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = str(datetime.datetime.today()).split(' ')[0]

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version=f'{version}',
    authenticator=authenticator
)
language_translator.set_service_url(f'{url}')

def englishToFrench(englishText):
    try:
        translation = language_translator.translate(englishText,model_id='en-fr').get_result()
        frenchText = translation["translations"][0]["translation"]
    except Exception as e:
        if 'Unable to validate payload size, the parameter \'text\' is null or empty.' in e.message:
            frenchText = ''
    return frenchText

def frenchToEnglish(frenchText):
    try:
        translation = language_translator.translate(frenchText,model_id='fr-en').get_result()
        englishText = translation["translations"][0]["translation"]
    except Exception as e:
        if 'Unable to validate payload size, the parameter \'text\' is null or empty.' in e.message:
            englishText = ''
    return englishText


