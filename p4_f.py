n=int(input("Enter limit : "))
list=[]
for i in range(n):
    y=int(input("Enter value : "))
    list.append(y)
mul=1
for i in list:
    mul=mul*i
print(f"Multiplication is : {mul}")