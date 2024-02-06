x=int(input("Enter number : "))
flag=False
for i in range(2,x):
    if x%i==0:
        flag=True
        break
if flag==True:
    print(x," is not prime number")
else:
    print(x," is prime number")