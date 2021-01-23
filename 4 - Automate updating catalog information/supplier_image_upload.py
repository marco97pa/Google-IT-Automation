#!/usr/bin/env python3
import requests
import os

"""
You have modified the fruit images through changeImage.py script.
Now, you will have to upload these modified images to the web server that is handling the fruit catalog.
To do that, you'll have to use the Python requests module to send the file contents to
the [linux-instance-IP-Address]/upload URL.

WARNING: If you can't connect to the server:
Run these commands in the ssh shell
 - sudo apt-get update
 - sudo apt install python-django-common
 - sudo systemctl start google-startup-scripts.service
(Source: https://www.coursera.org/learn/automating-real-world-tasks-python/discussions/weeks/4/threads/yh1c6lZjTiKdXOpWY_4itw)

"""

url = "http://localhost/upload/"
directory = "./supplier-data/images/"

os.chdir(directory)
for filename in os.listdir():
    if ".jpeg" in filename:
        with open(filename, 'rb') as opened:
            r = requests.post(url, files={'file': opened})