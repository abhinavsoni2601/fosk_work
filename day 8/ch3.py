# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:58:52 2019

@author: abhin
"""

from PIL import Image
import requests
from io import BytesIO

url = "http://forsk.in/images/Forsk_logo_bw.png"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.save("forsk-logo.png")
