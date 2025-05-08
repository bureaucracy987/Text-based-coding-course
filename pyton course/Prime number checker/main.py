lower=int(input("Enter a lower range:"))
upper=int(input("Enter a upper range:"))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2, num):
           if (i % num):
               break
    else:
        print(num)