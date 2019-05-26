from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
str1=input('enter your name')
str2=input("enter your batch")
str3=input("enter your date time")
img = Image.open("Forsk_logo_bw.png")
draw = ImageDraw.Draw(img)
selectFont = ImageFont.truetype("CaviarDreams_Bolditalic.ttf", size = 100)
draw.text( (500,0), "FORSK ID CARD", (0,128,0), font=selectFont)
selectFont = ImageFont.truetype("arial.ttf", size = 50)
draw.text( (20,150), "NAME"+str1, (0,0,225), font=selectFont)
draw.text( (20,200), "batch no"+str2, (0,0,225), font=selectFont)
draw.text( (220,200), "date"+str3, (0,0,0), font=selectFont)