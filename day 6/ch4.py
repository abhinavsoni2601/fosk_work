from functools import reduce
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

#for person in people:
#    if 'height' in person:
#        height_total += person['height']
#        height_count += 1
#def fun(x):
#    height_total = 0
#    height_count = 0
#    if 'height' in x:
#        height_total+=x['height']
#        height_count+=1
#        

list1=list(map(lambda y: y['height'],filter(lambda x: x['height'] if 'height' in x else print(''),people )))
reduce(lambda z,x:z+x,list1 )
print(len(list1))
