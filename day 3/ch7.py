str1=input('enter the first string')
str2=input('enter the sec string')
list1=list(str1)
list2=list(str2)
list1.sort()
list2.sort()
if (list1==list2):
    print(True)
else:
    print(False)