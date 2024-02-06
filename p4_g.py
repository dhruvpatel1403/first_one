n=int(input("Enter limit : "))
list=[]
for i in range(n):
    list.append(int(input("Enter data : ")))
##using sorting mathod....
list.sort()
print(f"Maximum number in list is : {list[n-1]}")