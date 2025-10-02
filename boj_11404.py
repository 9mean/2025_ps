import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
cities=[[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
  a,b,c=map(int,input().split())
  if cities[a][b]>c:
    cities[a][b]=c
for i in range(1,n+1):
  cities[i][i]=0
for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      cities[i][j]=min(cities[i][j],cities[i][k]+cities[k][j])

for i in range(1,n+1):
  for j in range(1,n+1):
    if cities[i][j]==sys.maxsize:
      print(0,end=' ')
    else:
      print(cities[i][j],end=' ')
  print()