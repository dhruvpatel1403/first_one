print("Enter the value of n : ",end="")
n=int(input())
def sum(z):
    if z==1:
        return(1)
    else:
        s=z+sum(z-1)
        return(s)
print(f"sum of first {n} natural number is : {sum(n)}")