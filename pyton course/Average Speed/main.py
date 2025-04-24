s1=int(input("Enter your first speed:"))
s2=int(input("Enter your second speed:"))
s3=int(input("Enter your third speed:"))
average=(s1+s2+s3)/3
print("The average speed is",average)
if s1<average:
 print("Speed 1 is is less than the average by the difference of",average-s1)
if s2<average:
 print("Speed 2 is is less than the average by the difference of",average-s2)
if s3<average:
 print("Speed 3 is is less than the average by the difference of",average-s2)