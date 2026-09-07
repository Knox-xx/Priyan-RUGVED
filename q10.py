cc=int(input("Enter a credit card number to check if its valid or not: "))
l=list(str(cc))
trs=l[::-1]
sum=0
for i in range(len(trs)):
    if i%2!=0:
        j=int(trs[i])*2
        if j>9:
          j=j-9
        sum+=j
    else:
        sum+=int(trs[i])
if sum%10==0:
    print("The credit card number is valid.")
else:
    print("The credit card number is not valid.")