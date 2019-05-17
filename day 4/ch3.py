import csv
list1 = []
water=0
dict1={}
with open('zoo.csv') as z1:
    zcsv=csv.reader(z1,delimiter=",")
    next(zcsv)
    for col in zcsv:
        print(col[2])
        list1.append(col[0])
        set2=set(list1)
        set3={'animal'}
        set2=set2.difference(set3)
        print(col[2])
        water+=int(col[2])
        
    
    print(set2)
print(water)
#    for x in zcsv:
#        print(x[2])
#        water+=int(x[2])
#    print(water)

#with open("zoo.csv") as z2:
#    z3= csv.DictReader(z2)
#    for x in z3:
#            print(x)
with open("zoo.csv","rt") as zoo:
    zoo1=csv.reader(zoo,delimiter=",")
    next(zoo1)
    for i in zoo1:
        if i[0] not in dict1:
            dict1[i[0]]=i[2]
        else:
            dict1[i[0]]=int(dict1[i[0]])+int(i[2])
    print(dict1)