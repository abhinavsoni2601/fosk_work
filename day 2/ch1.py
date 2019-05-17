str2=""
str1=input("enter the names with space")
for x in str1:
    if((x=='a')or(x=='e')or(x=='i')or(x=='o')or(x=='u')):
        continue
    else:
        str2=str2+x
list1=str2.split()
print(list1)