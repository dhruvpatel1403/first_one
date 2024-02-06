x=int(input("Enter limit : "))
while x>0:
    if x%2 == 0 and x%6 != 0:
        print(f"{x} is even")
        x=x-1
    elif x%2 == 1:
        print(f"{x} is odd")
        x=x-1
    else:
        print(f"{x} is divisible by 6")
        x=x-1