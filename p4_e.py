n=int(input("Enter limit : "))
list=[]
for i in range(2,n+1):
    flag=False
    for j in range(2,i):
        if i%j==0:
            flag=True
            break
    if flag==False:
        list.append(i)
print(f"prime number upto {n} is : {list}")