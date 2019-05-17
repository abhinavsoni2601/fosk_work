import csv
with open('asd1.txt') as x:
    y=csv.reader(x,delimiter=' ')
    for z in y:
        print(z[7])