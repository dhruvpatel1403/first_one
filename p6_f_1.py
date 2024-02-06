#1 funtion
# l=[1,2,3,4,5]
# def cube(x):
#     return x*x*x
# c=list(map(cube,l))
# print(c)
#2 lambda
# l=[1,2,3,4,5]
# c=list(map(lambda x:x*x*x,l))
# print(c)
# 3 list comprihension
l=[1,2,3,4,5]
res=[]
for i in l:
    res.append(i*i*i)
print(res)