str1=input("enter the days")
tuple1=('mon','tus','wed','thr','fri','sat','sun')
list1=str1.split()
list2=[]
for x in tuple1:
    if ((x  in list1) and (x  not in list2)):
         list2.append(x)

    elif x not in list1:
        list2.append(x)

print('input was')
print (tuple(list1))
print('output')
print(tuple(list2))     
