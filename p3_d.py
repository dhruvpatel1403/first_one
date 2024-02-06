n=int(input("Enter value of n : "))
list=[0,1]
for i in range(2,n):
    x = list[i-1] + list[i-2]
    list.insert(i,x)
for i in range (0,n):
    print(list[i],end="\t")