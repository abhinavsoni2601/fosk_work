str1=[]
var=0
list2=[]
with open('passwd')as file1:
    for line in file1:
        str1=line
        list2=str1.split(":")
        print(str(list2[0])+' '+str(list2[2]))
            
            