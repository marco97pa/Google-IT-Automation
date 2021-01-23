#!/usr/bin/env python3

"""
You will have to write a Python script named health_check.py that will run in the background monitoring
some of your system statistics: CPU usage, disk space, available memory and name resolution.
Moreover, this Python script should send an email if there are problems, such as:

Report an error if CPU usage is over 80%
Report an error if available disk space is lower than 20%
Report an error if available memory is less than 500MB
Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
"""

import shutil
import psutil
import requests
import socket
import emails
import os

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    hdd = du.free/du.total * 100
    return hdd

def check_cpu_usage():
    cpu = psutil.cpu_percent(1)
    return cpu

def available_memory_check():
  available = psutil.virtual_memory().available
  available_in_MB = available / 1024 ** 2 #convert to MB
  return available_in_MB

def email_warning(message):
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ["USER"])
  subject = message
  body = "Please check your system and resolve the issue as soon as possible."
  message = emails.generate_error_report(sender, receiver, subject, body)
  emails.send_email(message)

#Report an error if CPU usage is over 80%
if check_cpu_usage() > 80:
    email_warning("Error - CPU usage is over 80%")
#Report an error if available disk space is lower than 20%
if check_disk_usage("/") < 20:
    email_warning("Error - Available disk space is less than 20%")
#Report an error if available memory is less than 500MB
if available_memory_check() < 500:
    email_warning("Error - Available memory is less than 500MB")
#Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
if check_localhost() == False:
    email_warning("Error - localhost cannot be resolved to 127.0.0.1")