costprice=int(input("Please enter the cost price:"))
sellingprice=int(input("Please enter the selling price:"))
if (sellingprice>costprice):
    print("Profit!")
    pt=sellingprice-costprice
    print(pt)
else :
    print("No profit")