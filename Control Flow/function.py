# #function
# def convertion(usd):
#     return print(usd*122.18)
#
# convertion(float(input("Enter a number: ")))


#recursion-factorial
def factorial(n):
    if n==0:
        return 1
    else:
        print(n)    
        return n*factorial(n-1)
    print(factorial(n))

factorial(int(input("Enter a number: ")))

