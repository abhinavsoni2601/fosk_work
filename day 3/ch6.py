list1=['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m']
list2=[1,0,2,3,4,5,6,7,8,9]
var1=0
var2=0
dict1={'alph':var1,'int1':var2}
str1=input('ehter the string')
list3=list(str1)
for x in list3:
    if x in list1:
        dict1['alph']+=1
    if x in list2:
        dict1['int1']+=1
