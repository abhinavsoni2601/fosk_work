str1=input('enter the name of file ')
str1=str1+'.txt'
list2=[]
list2=[]
p=0
wordlen=0
var=0
stringlen=0
with open(str1,'rt') as file1:
    for line in file1:
        p+=1
        list2=line.split()
        var=len(list2)
        wordlen+=var
        var=len(line)
        stringlen+=var
    
print(str(p)+' '+str(wordlen)+' '+str(stringlen))