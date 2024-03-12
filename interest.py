#Compound interest
p=float(input("Enter amount to: "))
r=int(input("Enter the rate of interest : "))
t=int(input("Enter the number of years: "))
s=0
print("Year\tStarting Balance\tInterest\tEnding Balance")
for i in range(t):
    interest=float((p*r)/100)
    print(i+1,"\t",p,"\t","%14.2f"%round(interest,2),"\t","%10.2f"%(p+interest))
    p=p+interest
    s+=interest
print("Balance: ",round(p,2))
print("Total interest earned: ",s)
