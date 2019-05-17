list1=[12,24,35,24,88,120,155,88,120,155]
list2=[]
for x in list1:
    if x in list2:
        continue
    else:
        list2.append(x)
set1=set(list2)
print(set1)