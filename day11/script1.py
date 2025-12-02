#i need to writea script to get soem decrets for a secret amanger
# i need to hit a a api requests moudle use chesi call cehyyali and get that rteturned respi#onse and use


import requests
import logging
import json
import os


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def get_secrets():

    response = requests.get(api_url, timeout = 5)

    data = response.json()




api_url = os.envoron.get()


