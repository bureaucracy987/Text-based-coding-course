print("Enter marks obtained in 4 subjects:")
Maths=int(input("Maths:"))
English=int(input("English:"))
Science=int(input("Science:"))
Hindi=int(input("Hindi:"))
sum=Hindi+English+Science+Maths
print("Sum of the four subjects' marks:",sum)
perc=(sum/400)*100
print(end="Percentage Mark=")
print(perc)
