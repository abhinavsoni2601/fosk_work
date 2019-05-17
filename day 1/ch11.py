i=1
while(i<=100):
    if((i%3==0)and(i%5!=0)):
        print("buzz")
        
    else:
        if((i%5==0)and(i%3!=0)):
            print("fuzz")
        else:
            if((i%5==0)and(i%3==0)):
                print("buzzfizz")
            else:
                print(i)
    i=i+1
