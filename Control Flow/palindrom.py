#not from user
list1=[1,2,3,22,1]
list2=list1.copy()
list2.reverse()

if list2==list1:
    print("they are palindromes")
else:
    print("they are not palindromes")

#user input
l1=[]
size=int(input("enter the size of the element: "))
for i in range(size):
    el=int(input("enter the element: "))
    l1.append(el)

l2=l1.copy()
l2.reverse()

if l2==l1:
    print("they are palindromes")
else:
    print("they are not palindromes")
