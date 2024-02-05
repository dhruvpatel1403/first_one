x=int(input("Enter the 1st number : "))
y=int(input("Enter the 2nd number : "))
z=int(input("Enter the 3rd number : "))
if x>y and x>z:
    print(f"{x} is largest number")
elif y>x and y>z:
    print(f"{y} is largest number")
else:
    print(f"{z} is largest number")