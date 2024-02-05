n = int(input("Enter the limit : "))
def sum(x):
    if x==1:
        return(1)
    else:
        s = sum(x-1) + x
        return(s)

a = sum(n)
print(f"Sum is {a}")