sum=0
list1=[]
value=int(input('how many no will be there'))
while value>0:
    a=int(input('enter the number'))
   
    list1.append(a)   
    value=value-1
v=0
value=len(list1)
while (v!=(value)):
     if list1[v]==13:
         v=v+2
         
     else:
         sum=sum+list1[v]
         v=v+1
print(sum)