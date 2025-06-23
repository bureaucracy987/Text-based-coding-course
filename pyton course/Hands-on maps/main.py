numbers1=[1,2,3]
numbers2=[4,5,6]
result=map(lambda x,y:x+y,numbers1,numbers2)
print("Addition of two lists:",list(result))
nums=[1,8,9,10,7,2,3,5]
def sq(n):
    return n*n
square=list(map(sq,nums))
print("Square of all the numbers of the list",list(square))