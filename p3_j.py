x=int(input("Enter limit : "))
for i in range(1,x+2):
    for j in range(1,x+2):
        if j<i:
            print(f"{j}\t",end="")
    print() 