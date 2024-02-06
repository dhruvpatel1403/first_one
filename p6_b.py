from functools import reduce


o=int(input("Enter the first value : "))
n=int(input("Enter the last value : "))
list=[]
for i in range(o,n+1):
    list.append(i)
def sum(a,b):
    return(a+b)
print("Summation is : ",reduce(sum,list))