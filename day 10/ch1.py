from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
str1=input('enter your name')
img = Image.open("Forsk_logo_bw.png")
draw = ImageDraw.Draw(img)
selectFont = ImageFont.truetype("CaviarDreams_Bolditalic.ttf", size = 100)
draw.text( (20,0), "CERTIFICATE BY FORSK", (0,128,0), font=selectFont)
selectFont = ImageFont.truetype("arial.ttf", size = 50)
draw.text( (20,150), "This is a certificate for projectX given by FORSK LAB", (0,0,225), font=selectFont)
draw.text( (20,200), "given to", (0,0,225), font=selectFont)
draw.text( (220,200), str1, (0,0,0), font=selectFont)
img1 = Image.open("seal.png")
img.paste(img1,(0,400))
img2 = Image.open("sig.png")
img.paste(img2,(800,400))
img.save( "certi.png", "PNG", resolution=100.0)