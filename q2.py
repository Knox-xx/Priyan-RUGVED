w=input("Enter a word: ")
sw=sorted(w)
d={}
for c in sw:
    if c in d:
        d[c]+=1
    else:
        d[c]=1
print(d)
