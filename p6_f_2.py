l=[32,33,34,35,36]
#1
# def cel(x):
#     return((x-32)*(5/9))
# res=list(map(cel,l))
# print(res)
#2
# res=list(map(lambda x:(x-32)*(5/9),l))
# print(res)
# 3
res=[]
for i in l:
    res.append((i-32)*(5/9))
print(res)