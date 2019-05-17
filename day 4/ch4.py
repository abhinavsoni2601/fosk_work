str1=''
list2=[]
dict1={}
#with open('romeo2.txt','rt') as ro:
#    for x in ro:
#        list2=list1.append(x).split()
#   
    
fp1=open('romeo2.txt','rt')
str1=fp1.read()
list2=str1.split()
    
for item in list2:
    if item not in dict1:
            dict1[item]=1
    else:
        dict1[item]=int(dict1[item])+1
    
print(dict1) 
    