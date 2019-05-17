str1=input("enter the string")
str2=''
for x in str1:
    if((x=='a')or(x=='e')or(x=='i')or(x=='o')or(x=='u')):
        str2=str2+x
    else:
        str2=str2+x+'o'+x
    
print(str2)
