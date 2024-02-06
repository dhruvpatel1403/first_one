list1=[1,2,3,1,2,4,5]
def func_dups(list):
    set1=set()
    for i in list:
        if list.count(i) >= 2:
            set1.add(i)
    return(set1)
x=func_dups(list1)
print(x)