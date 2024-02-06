o=int(input("Enter first value of limit : "))
n=int(input("Enter last value of limit : "))
def itself(z):
    return(z)
def square(x):
    return(x*x)
def cube(y):
    return(y*y*y) 
func=[itself,square,cube]
for i in range(o,n+1):
    val=list(map(lambda x:x(i),func))
    print(val)