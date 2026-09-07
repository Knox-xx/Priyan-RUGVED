text = input("Enter the string: ").strip()
n = int(input("Enter n (length of each part): "))
if n <= 0:
    print("Error: n must be greater than zero.")
elif len(text) % n != 0:
    print("Error: The string cannot be divided into equal parts of " + str(n) + " characters.")
else:
    p = text[:n]
    l = len(text)//n 
    if p * l != text:
        print("Not a Repeating sequence")
    else:
        for i in range(0,l):
            print(p, end=" ") 