flag=0
str2=""
str1=input("enter the no ")
for x in str1:
    if(x=="-"):
        flag=1
        break
list1=str1.split()
var=len(list1)
inc=0
flage2=1
while var>0:
    str2=list1[inc]
    if(str2==str2[::-1]):
        flage2=0
        
    inc=inc+1
    var=var-1

if((flag==0)and(flage2==0)):
    print (True)
else:
    print (False)