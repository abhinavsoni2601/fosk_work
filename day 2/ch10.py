list2=[]
list1=[]
value=int(input('how many no will be there'))
while value>0:
    a=int(input('enter the number'))
    list1.append(a)
    if a not in list2:
        list2.append(a)
    
    value=value-1

sorted(list2)
m2=len(list2)
m3=int(m2/2)
print(list2[m3])
