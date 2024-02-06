tup=(1,2,3,1,1,2)
for i in tup:
    c=tup.count(i)
    if c>=2:
        print(f"{i} is appear {c} time in tuple...")