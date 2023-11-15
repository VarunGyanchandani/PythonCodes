def numbers():
    n1=int(input("Enter any number(n1):"))
    n2=int(input("Enter any number(n2):"))
    n3=int(input("Enter any number(n3):"))
    if n1>n2 and n1>n3:
        print("n1 is the greatest.")
    elif n2>n1 and n2>n3:
        print("n2 is the greatest.")
    else:
        print("n3 is the greatest.")
numbers()
