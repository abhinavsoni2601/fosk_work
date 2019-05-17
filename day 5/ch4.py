list1=[]
while True:
    str1=input('enter the string')
    if not str1:
        break
    import re
    output=re.findall(r'[a-z0-9_-]+@[a-z0-9]+\.[a-z]{2,3}',str1)
    list1+=output
list1.sort()
print(list1)