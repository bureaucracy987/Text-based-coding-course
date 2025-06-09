lst=[]
def word_matching(words):
    ctr=0
    
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)

    return ctr
    
count=word_matching(["abc","aba","quf","cfc","1221"])
print("Number of words having first and last letter same are",count)
print("list of words with first and last letter same are",lst)
