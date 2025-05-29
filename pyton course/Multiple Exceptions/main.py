try:
    num1=int(input("Enter any number"))
    num2=int(input("Enter any number"))
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("Division by zero is not possible .")
except ValueError:
    print("Please enter a numerical value")
except NameError as ex:
    print("The exception is",ex)
except:
    print("Some error occurred")
finally:
    print("I will not stop anyhow.")

