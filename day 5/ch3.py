while True:
    str1=input('enter the string')
    if not str1:
        break
    
    import re
    if re.findall(r'^[456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$',str1):
        print(True)
    else:
        print(False)