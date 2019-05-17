str1=input('enter the number')
import re
if re.match(r'^[+-]?[0-9]+\.[0-9]+$',str1):
    print(True)
else:
    print(False)
