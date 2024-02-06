n=[-3,1,6]
def sumprimes(x):
    sum=0
    for i in x:
        if i==1 or i<0:
            continue
        else:
            flag=False
            for j in range(2,i):
                if i%j==0:
                    flag=True
                    break
            if flag==False:
                sum=sum+i
    return(sum)
print("sum of rprime number is : ",sumprimes(n))
