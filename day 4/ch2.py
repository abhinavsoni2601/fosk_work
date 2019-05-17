while True:
    str1=input('enter the name of student')
    if not str1:
        break
    with open('absentlist1.txt','a+') as fp1:
        fp1.write(str1+"\n")
        