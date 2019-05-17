oldlist=['as','qw','zx']
newlist=['zx','qw','fg']
set1=set(oldlist)
set2=set(newlist)
outset=set1.difference(set2)
print(outset)
