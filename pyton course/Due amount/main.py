def due_amount(a,b):
    return b-a
p=int(input("Please enter the amount to be paid:"))
q=int(input("Please enter the amount you have paid:"))
print("Your due amount is",due_amount(p,q))