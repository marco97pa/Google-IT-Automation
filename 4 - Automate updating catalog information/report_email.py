#!/usr/bin/env python3
import os, datetime
from reports import generate_report
import emails

""" Create another script named report_email.py to process supplier fruit description data from
 supplier-data/descriptions directory. 

 First process the text data from the supplier-data/descriptions directory into the format below as PDF:
    name: Apple
    weight: 500 lbs
    [blank line]
    name: Avocado
    weight: 200 lbs
    [blank line]
    ...

 Then send the generated PDF via email with these details:
    From: automation@example.com
    To: username@example.com
    Replace username with the username given in the Connection Details Panel on the right hand side.
    Subject line: Upload Completed - Online Fruit Store
    E-mail Body: All fruits are uploaded to our website successfully. A detailed list is attached to this email.
    Attachment: Attach the path to the file processed.pdf
"""


pdf = "/tmp/processed.pdf"
directory = "./supplier-data/descriptions/"

def get_contents(directory):
    output = ""

    os.chdir(directory)
    for filename in os.listdir():
        if ".txt" in filename:
            with open(filename, 'r') as opened:
                #Read from file
                data = opened.read()
                #Split lines
                data = data.split("\n")
                #Get informations
                name = data[0]
                weight = data[1]
                #Append
                output += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"

    return output

if __name__ == "__main__":
    #Get date
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    #Make title
    title = "Process Updated on " + current_date 

    #Generate contents for pdf body
    contents = get_contents(directory)
    #Generate report as PDF
    generate_report(pdf, title, contents)

    #Generate email information
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ["USER"])
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = pdf
    
    #Generate email
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)