import requests
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 23:01:23 2022

@author: Muhmmad Fawad Aleem
"""

GENDER = "male"
WEIGHT_LBS = 190.00
HEIGHT_FTS = 5.9166667
AGE = 28


APP_ID = "6bad03cd"
APP_KEY = "7c9059b6e4d9e5e17baac6d4284ab625"

excersice_endpoint = " https://trackapi.nutritionix.com/v2/natural/exercise"

ex_text = input("WHAT EXCERSICE DID YOU DO: ")

header = {
            "x-app-id": APP_ID,
            "x-app-key":APP_KEY
            }

parameter = {
                "query":ex_text,
                "gender":GENDER,
                "weight_lbs":WEIGHT_LBS,
                "height_ft":HEIGHT_FTS,
                "age":AGE
            }

res = requests.post(excersice_endpoint, json=parameter, headers=header)
result = res.json()
print(result)