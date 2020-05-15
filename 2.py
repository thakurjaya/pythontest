a=int(input("enter a number"))
l=list()

for i in range(0,2*a):
    if i%2!=0:
       l.append(i)
for i in l:
    print(i,end=" ")

    
