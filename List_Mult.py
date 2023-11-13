def mult_2(p):
    p=p*2
    return p
l=[1,2,3,4,7,8,9,0]
a=list(map(mult_2,l))
print(a)
new_l=[]
n=int(input("Enter the number of elements you want to add in the list:"))
for i in range(n):
    new_l.append(int(input("Enetr the elements:")))
b=list(map(mult_2,new_l))
print(b)