#square
pat=int(input("enter a number: "))
for i in range(1,pat+1):
    for j in range(1,pat+1):
        print("*",end=" ")
    print()

#right triangle
pat=int(input("enter a number: "))
for i in range(1,pat+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

#print reverse no
no=int(input("enter a number: "))
for i in range(no,0,-1):
    print (i,end=" ")