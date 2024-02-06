list1=[1,2,3]
list2=[1,4,9]
dict={}
for i in list1:
    for j in list2:
        if j in dict.values():
            continue
        else:
            dict[i]=j
            break
print(dict)