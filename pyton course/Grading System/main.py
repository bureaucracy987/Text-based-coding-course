Hindi=int(input("Enter the marks obtained in Hindi:"))
English=int(input("Enter the marks obtained in English:"))
Science=int(input("Enter the marks obtained in Science:"))
Maths=int(input("Enter the marks obtained in Maths:"))
Computer=int(input("Enter the marks obtained in Computer:"))
total=Hindi+English+Science+Maths+Computer
print(total)
avg=total/5
if avg>91 and avg<100:
 print("Your grade is A1.")
elif avg>81 and avg<91:
 print("Your grade is A2.")
elif avg>71 and avg<80:
 print("Your grade is A3.")
elif avg>61 and avg<70:
 print("Your grade is A4.")
elif avg>51 and avg<60:
 print("Your grade is A5.")
elif avg>41 and avg<50:
 print("Your grade is B1.")
elif avg>0 and avg<40:
 print("Your grade is B2.")
else:
 print("Unidentified Error!!!")