f=open("C:\\Users\\DELL\\Desktop\\New Text Document.txt")
for i in range(0,4):
    x=list(f.readline())
    a=int(x[0])
    b=int(x[1])
    print(f"sum is {a+b} and mul is {a*b}")