#Aritmatic operators
x=int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))
print("1). Add\n2). Sub\n3). Mul\n4). Div\n5). Int Div")
print("Enter your choice : ",end="")
ch=int(input())
if ch==1:
    z=x+y
    print(f"The Sum is : {z}")
elif ch==2:
    z=x-y
    print(f"The Div is : {z}")
elif ch==3:
    z=x*y
    print(f"The Mul is : {z}")
elif ch==4:
    z=x/y
    print(f"The Div is : {z}")
elif ch==5:
    z=x//y
    print(f"The Int Div is : {z}")
else:
    print("Enter valid choice...")