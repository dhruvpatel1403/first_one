n=int(input("Enter limit : "))
list=[]
for i in range(n):
    list.append(int(input("Enter data : ")))
list.sort()
print(f"Second smallest number in list is : {list[1]}")