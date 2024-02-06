n=int(input("Enter limit : "))
list1=[]
for i in range(2,n+1):
    list1.append(i)
def prime(x):
        flag=False
        for j in range(2,x):
            if x%j == 0:
                flag=True
                break
        if flag==False:
            return(x)
filtered=list(filter(prime,list1))
for i in filtered:
    print(i)