def anag(s1,s2):
    cs1=s1.lower()
    cs2=s2.lower()
    return sorted(cs1)==sorted(cs2)
x1=input("Enter the first string: ")
x2=input("Enter the second string: ")
print(anag(x1,x2))