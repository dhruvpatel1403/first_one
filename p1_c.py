#swapping two number without using third variable
x=int(input("Enter the value of x : "))
y=int(input("Enter the value of y : "))
x=x+y
y=x-y
x=x-y
print(f"The values of x and y after swaping : x = {x} , y = {y}")