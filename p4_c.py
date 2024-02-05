x=int(input("Enter limit : "))
list=[]

for i in range(0,x):
    y=int(input("Enter data : "))
    list.append(y)
print("Our list is : ",list)
for i in range(0,x):
    rev=0
    a=list[i]
    while a>0:
        b=a%10
        rev=rev*10+b
        a//=10
    if rev==list[i]:
        print(f"{list[i]} is palindrom number")
    else:
        print(f"{list[i]} is not palindrom number")