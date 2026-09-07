n=int(input("Enter the value of n for the pattern: "))
k=n-1
for i in range(1, n+1):
    print(" " * k, end="")
    k-=1
    print("* " * i)
k=0
for j in range(n, 0, -1):
    print(" " * k, end="")
    k+=1
    print("* " * j)  