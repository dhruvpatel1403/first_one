list=[1,2,3,4,5]
list2=[]
for i in range(0,5):
    a=list.pop()
    list2.append(a)
list2.reverse()
print(list2)