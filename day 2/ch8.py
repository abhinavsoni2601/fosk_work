sum=0
mul=1 

list2=[]
list1=[]
value=int(input('how many no will be there'))
while value>0:
    a=int(input('enter the number'))
    sum=sum+a
    mul=mul*a
    list1.append(a)
    if a not in list2:
        list2.append(a)
    
    value=value-1

print((sum))
print((mul))
print("no duplicate")
print(list2)
print(sorted(list1))
print(min(list1))
print(max(list2))