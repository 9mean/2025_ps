n,m=map(int,input().split())
a=[[0]*(n+1)]
b=[[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
  a_row=[0]+[int(x) for x in input().split()]
  a.append(a_row)
for i in range(1,n+1):
  for j in range(1,n+1):
    b[i][j]=b[i-1][j]+b[i][j-1]-b[i-1][j-1]+a[i][j]
for i in range(m):
  x1,y1,x2,y2=map(int,input().split())
  res=b[x2][y2]-b[x1-1][y2]-b[x2][y1-1]+b[x1-1][y1-1]
  print(res)