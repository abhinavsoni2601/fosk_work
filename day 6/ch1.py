while True:
    str1=input('enter the string')
    if not str1:
        break
    list2=[]
    for  x in str1:
        if x==x[::-1]:
            list2.append(True)
        else:
            list2.append(False)
    #filter(x,list1)
print(any(list2))