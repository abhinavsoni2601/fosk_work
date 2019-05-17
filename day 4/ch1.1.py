with open('a.jpg','rb') as f1:
    with open('c.jpg','wb') as f2:
        for line in f1:
            f2.write(line)

