o=int(input("Enter first value of limit : "))
n=int(input("Enter last value of limit : "))
l=[]
for i in range(o,n+1):
    l.append(i)
def arm(x):
    s=0
    b=x
    m=x
    count=0
    while m>0:
        m //= 10
        count= count +1
    while x>0:
        a=x%10
        s=s+a**count
        x//=10
    if b==s:
        return(b)
ar=list(map(arm,l))
res=[]
for i in ar:
    if i!=None:
        res.append(i)
print(res)