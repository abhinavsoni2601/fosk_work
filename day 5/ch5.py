import re
with open('simpsons_phone_book.txt') as file1:
    for str1 in file1:
        if re.findall(r'^J[a-z]*\ Neu',str1):
            print(str1)
    
    
