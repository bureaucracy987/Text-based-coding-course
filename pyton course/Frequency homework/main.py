exam={"Rahul":48,
      "Padma":50,
      "Debarjya":50,
      "Nirvaan":45,
      "Vivan":48}
print("The marks of the following students are",str(exam))
v=50
res=0
for i in exam:
    if exam[i]==v:
        res+=1
print("The number of boys who got full marks are",res)
