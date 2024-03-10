def prime():
    x=int(input("Enter any number:"))
    for i in range(2,x):
        if(x%i==0):
            print("Number is not a prime number.")
            break
    else:
        print("Number is a prime number.")
prime()
