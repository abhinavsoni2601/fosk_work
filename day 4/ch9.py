import csv
with open('passwd')as file1:
    file2=csv.reader(file1,delimiter=":")
    for col in file2:
        print (str(col[0])+' '+str(col[2]))