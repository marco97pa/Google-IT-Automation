You work for an online fruit store, and you need to develop a system that will update the catalog information with data provided by your suppliers. When each supplier has new products for your store, they give you an image and a description of each product.

Given a bunch of images and descriptions of each of the new products, you’ll:
- Upload the new products to your online store. Images and descriptions should be uploaded separately, using two different web endpoints.
- Send a report back to the supplier, letting them know what you imported.

Since this process is key to your business's success, you need to make sure that it keeps running! So, you’ll also:
- Run a script on your web server to monitor system health.
- Send an email with an alert if the server is ever unhealthy.

## Details
You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.

Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs). 

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong. 

## What you'll do
- Write a script that summarizes and processes sales data into different categories 
- Generate a PDF using Python
- Automatically send a PDF by email 
- Write a script to check the health status of the system 

## Libraries needed
- [Python Image Library (PIL)](https://pillow.readthedocs.io/) - [Tutorial](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html)
- [Requests (HTTP client library)](https://requests.readthedocs.io/) - [Quickstart](https://requests.readthedocs.io/en/master/user/quickstart/)
- [ReportLab (PDF creation library)](https://www.reportlab.com/docs/reportlab-userguide.pdf)
- [email (constructing email)](https://docs.python.org/3/library/email.examples.html)
- [psutil (processes and system utilization)](https://psutil.readthedocs.io/)
- [shutil (file operations)](https://docs.python.org/3/library/shutil.html)
- [smtplib (sending email)](https://docs.python.org/3/library/smtplib.html)