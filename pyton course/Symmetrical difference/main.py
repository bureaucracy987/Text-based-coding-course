setx={"blue","green"}
sety={"yellow","blue"}
print("Original set elements:",setx,sety)
print("Intersection of two sets:")
setz=setx.intersection(sety)
print(setz)
print("Union of two sets")
seta=setx.union(sety)
print(seta)
print("Symmetrical difference of two sets:")
sete=seta-setz
print(sete)