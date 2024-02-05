x=int(input("Enter value : "))
j=x
i=x
count=0
while i>0:
    i //= 10
    count= count +1
a=0
while x>0:
    b=x%10
    a=a+b**count
    x //= 10
if a == j:
    print("Number is armstrong number")
else:
    print("Number is not armstrong number")