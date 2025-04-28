units=int(input("Please enter the number of units you consumed:"))
if(units<50):
  amount=units*2.60
  print(amount)
elif(units<100):
  amount=units*3.40
  print(amount)
elif(units<200):
  amount=units*4.29
  print(amount)
else:
  amount=units*5.99
  print(amount)