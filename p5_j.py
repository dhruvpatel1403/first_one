x=int(input("Enter the value : "))
dict={1:1,2:4,3:9,4:16}
z=False
for i in dict.keys():
    if x==i:
        z=True
        break
if z==True:
    print("key is already present in dictionary")
else:
    print("key is not present in dictionary")