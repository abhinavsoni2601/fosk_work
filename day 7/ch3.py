var1=int(input("enter the usd amount"))
url="https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=583ef234e0c427815a21"
import requests
responce=requests.get(url)
import json
output=responce.json()
print(output['USD_INR']*var1)