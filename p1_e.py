#find area of reactangel and circle
print("Enter 1 to find area of reactangel and 2 for find are of circle : ",end="")
x=int(input())
if x == 1:
    print("Enter lenth of rectangle : ",end="")
    l=int(input())
    print("Enter Height of rectangle : ",end="")
    h=int(input())
    a=l*h
    print(f"Area of Rectangle is : {a}")
elif x == 2:
     print("Enter radius of circle : ",end="")
     r=int(input())
     a=(22/7)*r*r
     print(f"Area of circle is : {a}")
else:
    print("Enter valid choice.....")