matrix =[]
maxlst = []
matrix = [list(map(int,input().split())) for _ in range(9)]

for i in range(9):
    maxlst.append(max(matrix[i]))

print(max(maxlst))
print(maxlst.index(max(maxlst))+1,matrix[maxlst.index(max(maxlst))].index(max(maxlst))+1)