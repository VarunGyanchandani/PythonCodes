p=int(input("Enter the principle amount:"))
r=float(input("Enter the rate of interest:"))
t=int(input("Enter the time period:"))
A=p*(1+(r/100))**t
c=A-p
print("Compound Interest is:",int(c))
print("Amount to be paid is:",int(A))