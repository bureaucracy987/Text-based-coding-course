Amount=int(input("Please enter the amount of money which is to be counted:"))
note_1=Amount//500
note_2=(Amount%500)//200
note_3=((Amount%500)%200)//100
note_4=(((Amount%500)%200)%100)//50
note_5=((((Amount%500)%200)%100)%50)//20
note_6=(((((Amount%500)%200)%100)%50)%20)//10
note_7=((((((Amount%500)%200)%100)%50)%20)%10)//5
print("Notes of 500 rupees:",note_1)
print("Notes of 200 rupees:",note_2)
print("Notes of 100 rupees:",note_3)
print("Notes of 50 rupees:",note_4)
print("Notes of 20 rupees:",note_5)
print("Notes of 10 rupees:",note_6)
print("Notes of 5 rupees:",note_7)