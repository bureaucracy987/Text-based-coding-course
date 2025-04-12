Amount=int(input("Please enter the amount of cash you want to withdraw:"))
note_1=Amount//1000
note_2=(Amount%1000)//500
note_3=((Amount%1000)%500)//200
note_4=(((Amount%1000)%500)%200)//100
note_5=((((Amount%1000)%500)%200)%100)//50
note_6=(((((Amount%1000)%500)%200)%100)%50)//10
print("Notes of 1000 rupees:",note_1)
print("Notes of 500 rupees:",note_2)
print("Notes of 200 rupees:",note_3)
print("Notes of 100 rupees:",note_4)
print("Notes of 50 rupees:",note_5)
print("Notes of 10 rupees:",note_6)