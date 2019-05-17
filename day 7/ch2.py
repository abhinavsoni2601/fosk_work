url1=" "
url2=" "
url3=" "
import json
import requests
str1=input('enter the name of city')
url1="http://api.openweathermap.org/data/2.5/weather?q="
url1=url1+str1
url3="&appid=5bd3b3302e17b1fb27cd720ccebff986"
url1=url1+url3

output=requests.get(url1)
output2=output.json()
#print(output2)
print("cordinate are {} weather is {} Wind Speed {} Sunset Rise{} and Set timing {}".format(output2["coord"],output2["weather"],output2["wind"],output2["sys"]["sunrise"],output2["sys"]["sunset"])) 


from PIL import Image
import requests
from io import BytesIO

url = "http://forsk.in/images/Forsk_logo_bw.png"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.save("forsk-logo.png")

