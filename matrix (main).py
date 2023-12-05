rows=int(input())
col=int(input())
mat=[]
print("ENter matrix elements: ")
for i in range(rows):
    a=[]
    for j in range(col):
        a.append(int(input()))
    mat.append(a)
print("Input matrix is: ")
for i in range(rows):
    for j in range(col):
        print(mat[i][j],end=" ")
    print()
rs = [sum(i) for i in mat]
cs = [sum(i) for i in zip(*mat)]
ds = sum(mat[i][i] for i in range(min(rows,col)))

for i, rjs in enumerate(rs):
    print(f"rows{i+1} ",rjs)
for i, cjs in enumerate(cs):
    print(f"row{i+1} ",cjs)
print("Diagonal sum is : ",ds)

print("Transpose matrix is: ")
for i in range(col):
    for j in range(rows):
        print(mat[j][i],end=" ")
    print()
        
