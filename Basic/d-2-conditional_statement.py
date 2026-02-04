#odd_even
num= int(input("Enter a number= "))
if num%2==0:
    print("even")
else:
    print("odd")

#largerst number betweeen 3
no= int(input("Enter 1st number= "))
no2= int(input("Enter 2nd number= "))
no3= int(input("Enter 3rd number= "))
if no>no2 and no>no3:
    print("the "+ str(no) +" is largest")
elif no2>no and no2>no3:
    print("the "+ str(no2)+ " is largest")
else:
    print("the " + str(no3) + " is largest")

#Simple Login System
un= str(input("Enter Your Username= "))
pw= int(input("Enter Your Password= "))
if un== "mugdha" and pw==2203007 :
    print("you are logged in")
elif un== "mugdha" :
    print("invalid password")
elif pw==2203007 :
    print("invalid username")
else:
    print("wrong username and password")

#super simple grade for tenary statement
mark= input("Enter your mark= ")
print ("passed") if mark>= str(33) else print("failed")

#cleaver if
sal=float(input("Enter your salary= "))
tax= sal*(0.2,0.3) [sal>=10000]
print("your tax is",tax)

