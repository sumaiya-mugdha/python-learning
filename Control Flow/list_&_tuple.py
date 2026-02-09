#list
student= ["Mew", 2, 14.7]
print("your marks is: "+ str(student[2]))
print("your name is: "+ str(student[0]))

#list methods
listing= [4, 2, 6, 2]
print("your list is: " + str(listing))

listing.append(6)
print("your list2 is: " + str(listing))

listing.insert(2,5)
print("your list3 is: " + str(listing))

listing.reverse()
print("your list4 is: " + str(listing))

listing.pop(3)
print("your list5 is: " + str(listing))

listing.sort()
print("your list6 is: " + str(listing))

listing.clear()
print("your list7 is: " + str(listing))

nlist=[1,5,2,5,3,5,4]
b=nlist.count(5)
print("your 5 is: " + str(b)+" times")

#tuple
tup=(1, 2, 3, 4, 6, 7, 6, 2, 6,)
print("your tuple is: " + str(tup))

#tuple method
x= tup.count(6)
print(x)
print(tup.index(6))

#Convert list → tuple → list
list4=['i','l','o','v','e','u']
tup=tuple(list4)
print("your tuple is: " + str(tup))

tup2= ('t','h','o','v','e','u')
lst=list(tup2)
print("your list is: " + str(lst))

#take input from user using loop
l=[]
size=int(input("enter the size of the list: "))

for i in range(size):
    x=int(input("enter the elements: "))
    l.append(x)
print(l)