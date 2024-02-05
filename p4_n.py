list1=[[1,2,3],[4,5,6],[7,8,9]]
list2=[[4,5,6],[7,8,9],[1,2,3]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(list1)):
    for j in range(len(list1[0])):
        result[i][j]=list1[i][j]+list2[i][j]
print(result)