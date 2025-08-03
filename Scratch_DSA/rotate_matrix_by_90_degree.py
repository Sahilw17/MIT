mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n=len(mat)
for i in range(0,len(mat)):
    for j in range(0,len(mat)):
        print(f"{mat[i][j]}",end=" ")
    print()

for i in range(0,n):
    for j in range(i+1,n):
        mat[i][j],mat[j][i]=mat[j][i],mat[i][j]


for i in range (0,n):
      mat[i].reverse()

print()

for i in range(0,len(mat)):
    for j in range(0,len(mat)):
        print(f"{mat[i][j]}",end=" ")
    print()

