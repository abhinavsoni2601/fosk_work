import string
str2=''
str1=input("enter the string").lower()
str3=list(string.ascii_lowercase)
for x in str1:
    if x in str3 and x not in str2:
       str2=str2+x 
     
    else :
        continue
    
str4=sorted(str2)
if(str4==str3):
    print('PANGRAM')
else:
    print("not PANGRAM")
    