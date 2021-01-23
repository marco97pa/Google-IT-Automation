#!/usr/bin/env python3
import requests
import os

"""
Write a Python script named run.py to process the text files (001.txt, 003.txt ...)
from the supplier-data/descriptions directory.
The script should turn the data into a JSON dictionary by adding all the required fields,
including the image associated with the fruit (image_name), and uploading it
to http://[linux-instance-external-IP]/fruits using the Python requests library.
"""

url = "http://localhost/fruits/"
directory = "./supplier-data/descriptions/"

os.chdir(directory)
for filename in os.listdir():
    if ".txt" in filename:
        with open(filename, 'r') as opened:
            #Grab the filename without extension
            fruit_name = os.path.splitext(filename)[0]
            #Read from file
            data = opened.read()
            #Split lines
            data = data.split("\n")
            #Make a dictionary
            fruit_dict = {"name": data[0], "weight": int(data[1][:-4]), "description": data[2], "image_name": fruit_name + ".jpeg"}
            #Post to the server
            print(fruit_dict)
            response = requests.post(url, json=fruit_dict)
            response.raise_for_status()
            print("Response returned " + str(response.status_code) + "\n\n")