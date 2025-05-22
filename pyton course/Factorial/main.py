def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter any number"))
if num<0:
    print("Factorial doen't exist for negative numbers")
else:
    print("The factorial of",num,"is",factorial(num))