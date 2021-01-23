#!/usr/bin/env python3

"""Working with supplier images
In this section, you will write a Python script named changeImage.py to process the supplier images.
You will be using the PIL library to update all images within ~/supplier-data/images directory to
the following specifications:

- Size: Change image resolution from 3000x2000 to 600x400 pixel
- Format: Change image format from .TIFF to .JPEG
"""

import os
from PIL import Image

directory = "./supplier-data/images/"

os.chdir(directory)
for filename in os.listdir():
   img = Image.open(filename)
   img = img.convert('RGB')
   img = img.resize((600,400))
   new_name = filename[:-5] + ".jpeg"
   print("Saving " + new_name)
   img.save(new_name, "jpeg")