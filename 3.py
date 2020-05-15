a=int(input("enter a number"))
l=list()
if a==1 or a==2:
    print("1")
else:    
    for i in range(0,2*a):
        if i%2!=0:
           l.append(i)
    for i in l:
        print(i,end=" ")

    
