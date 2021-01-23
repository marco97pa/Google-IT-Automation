#! /usr/bin/env python3

import os
import requests

feedbacks = []
corpweb_external_IP = "INSERT.YOUR.IP.HERE"

""" 
    List all .txt files under /data/feedback directory that contains
    the actual feedback to be displayed on the company's website. 
"""
path = "/data/feedback/"
dirs = os.listdir(path)

""" 
    Now you have a list that contains all of the feedback files from the path /data/feedback.
    Traverse over each file and, from the contents of these text files, create a dictionary by keeping
    title, name, date, and feedback as keys for the content value, respectively.
"""
for file in dirs:
    print()
    print("Reading " + file)
    file_r = open(path + file, 'r')
    lines = file_r.readlines()
    
    feedback = {}
    feedback["title"] = lines[0].strip()
    feedback["name"] = lines[1].strip()
    feedback["date"] = lines[2].strip()
    feedback["feedback"] = lines[3].strip()
    feedbacks.append(feedback)

    print(feedback)

    """
        Use the Python requests module to post the dictionary to the company's website.
        Use the request.post() method to make a POST request to http://<corpweb_external_IP>/feedback.
        Replace <corpweb_external_IP> with corpweb's external IP address.
    """
    response = requests.post("http://" + corpweb_external_IP + "/feedback/", json=feedback)
    # Check that the server answers with 201 (SUCCESS)
    print("Server answered with: " + str(response.status_code))
