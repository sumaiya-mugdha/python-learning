no=[1,2,3,4,5]
for i in no:
    print(i)

veg=["spanich","potato","brinjal"]
for i in veg:
    print(i)

#charecter for loop searching
strg="mugdha"
for i in strg:
    if i=="k":
        print("found")
        break
else:
    print ("end")


#range
seq= range(10) #####  for i in range(10):----also valid
for i in seq:
    print (i)

for i in range(3,25,3):
    print (i)

#multipication table of a number using for and range
no= int(input("Enter a number: "))

for i in range(11):
    print(str(no)+" X "+str(i)+" = "+str(no*i))

#pass statement
for i in range(11):
    pass
print("Hi")