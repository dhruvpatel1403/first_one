from functools import reduce


list=[1,22,3,4,5]
def Max(a,b):
    if a>b:
        return(a)
    else:
        return(b)
print("Maximum number is : ",reduce(Max,list))