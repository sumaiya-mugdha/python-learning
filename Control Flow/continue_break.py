# #seach a no for break statement
a= [1,2,4,9,16,25,36,49,64,81,100]
no=int(input("enter the searching number= "))
i=0
while i<len(a):
    if a[i] == no:
        print("found at index "+ str(i+1))
        break
    i = i + 1
else:
    print("not found")


# for even -continue
i=0
while i<=10:
    if i%2 !=0:
        i=i+1
        continue
    print (i)
    i=i+1

