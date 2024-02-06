l=["a1","a","B","c","1"]
# 1
# def al(x):
#     if x.isalpha() == True:
#         return(x)
# res=list(map(al,l))
# res2=[]
# for i in res:
#     if i!=None:
#         res2.append(i)
# print(res2)
# 2
# res=list(filter(lambda x:x.isalpha(),l))
# print(res)
res=[]
for i in l:
    if i.isalpha()==True:
        res.append(i)
print(res)