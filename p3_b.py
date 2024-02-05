"""n=int(input("Enter total number you want to enter : "))
sum=0
for i in range(0,n):
    a=int(input("Enter number : "))
    sum = sum + a

print(f"Sum is {sum}")"""
n=int(input("n : "))
list=[]
sum=0
for i in range(0,n):
    y=int(input("Enter number : "))
    list.insert(i,y)
for i in range(0,n):
    sum = sum + list[i]
print(f"Sum is {sum}")