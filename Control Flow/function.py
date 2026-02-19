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
        return n*factorial(n-1)

factorial(int(input("Enter a number: ")))

