#productlist=['apple','mango','banana','graps']
#prizelist=[60,70,50,60]
##str1=input('enter the input')
##list1=str1.spilt()
#dict1={}
#counter=0
#for x in productlist:
#    dict1[x]=prizelist[counter]
#    counter=counter+1
#
dict2={}
while True:
    str2=input('enter the value')
    if not str2:
        break
    list1=str2.split()
    var=''.join(list1[:-1])
    if var in dict2:
        dict2[var]+=int(list1[-1])
    else:
        dict2[var]=int(list1[-1])
    
  
     
dict2.items()