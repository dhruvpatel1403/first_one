x=int(input("Enter limit : "))
for i in range(0,x+1):
    for j in range(0,x+1):
        if j<i:
            print("*",end="\t")
    print()