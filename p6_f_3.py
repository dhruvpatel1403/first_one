l=[-2,-1,0,1,2,3]
#1
# def pos(x):
#     if x>0:
#         return(x)
# res=list(map(pos,l))
# res2=[]
# for i in res:
#     if i!=None:
#         res2.append(i)
# print(res2)
# 2
# res=list(filter(lambda x:(x>0),l))
# print(res)
# 3
res=[]
for i in l:
    if i>0:
        res.append(i)
print(res)