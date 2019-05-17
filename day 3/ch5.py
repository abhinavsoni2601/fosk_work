str1=input('enter the string')
list1=list(str1)
dict1={}
for x in list1:
    if x not in dict1:
        dict1[x]=1
    else:
        dict1[x]+=1
dict1.items()
        