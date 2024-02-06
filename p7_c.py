f=open("C:\\Users\\DELL\\Desktop\\New Text Document.txt")
for i in range(3):
    x=f.readline()
    if x.isupper():
        print("this is header")
    elif x[0:1]=="/" and x[1:2]=="/":
        print("this is comment line")
    else:
        print(x)
