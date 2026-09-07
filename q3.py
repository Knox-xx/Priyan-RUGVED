n=input("Enter a number to check if its hill no. or not")
k=1
i=0
l=list(n)
m=max(l)
ii=l.index(m)
for i in range (ii):
    if l[i]>l[i+1]:
        k=0
        break
if (k):
    j=ii
    for j in range (ii,len(l)-1):
        if l[j]<l[j]:
            k=0
            break
if(k):
    print("Hill number")
else:
    print("Not a Hill number")

    
