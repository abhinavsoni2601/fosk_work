dict1={}
list2=[]
out=0
while True:
    str1=input('enter the number')
    if not str1:
        break
    list1=str1.split()
    var1=''.join(list1[:-1])
    var2=list1[-1]
    dict1[var1]=int(var2)
    
for x in dict1.values():
    if x in range(13,20):
        continue
    else:
        out+=x
print(out)
