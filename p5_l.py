x=int(input("Enter key : "))
dict={1:1,2:4,3:9}
if x in dict.keys():
    dict.pop(x)#del dict[x]
print(dict)