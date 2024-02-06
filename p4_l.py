list1=[1,2,3,4]
list2=[5,7]
def function(a,b):
    y={*set(a)}
    z={*set(b)}
    c=y.intersection(z)
    if len(c) == 0 :
        return(False)
    else:
        return(True)
print(function(list1,list2))
