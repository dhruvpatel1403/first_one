n=int(input("Enter limit : "))
list=[]
for i in range(n):
    d=int(input("Enter data : "))
    list.append(d)
m=int(input("Enter last number : "))
if m <= len(list):
    list2=[]
    for i in range(m):
        a=list[i]
        if a%2==0:
            list2.append(a)
else:
    print("Enter valid number...")
print(list2)