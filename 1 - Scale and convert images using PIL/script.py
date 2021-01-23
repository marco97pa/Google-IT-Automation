#!/usr/bin/python3
import os
from PIL import Image

input_dir = "./images"
output_dir = "/opt/icons/"

os.chdir(input_dir)
for filename in os.listdir():
   img = Image.open(filename)
   img = img.resize((128,128))
   img = img.rotate(90)
   print("Saving " + filename)
   img.convert('RGB').save(output_dir + filename, "jpeg")
