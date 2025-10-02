import sys
input=sys.stdin.readline

n,m=map(int,input().split())
edges=[]

distance=[sys.maxsize]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    edges.append((a,b,c))

distance[1]=0
for _ in range(n-1):
    for start,end,time in edges:
      if distance[start]!=sys.maxsize and distance[end]>distance[start]+time:
          distance[end]=distance[start]+time

flagCycle=False
for start,end,time in edges:
      if distance[start]!=sys.maxsize and distance[end]>distance[start]+time:
          flagCycle=True
          break
if not flagCycle:
    for i in range(2,n+1):
        if distance[i]==sys.maxsize:
            print(-1)
        else:
            print(distance[i])
else:
    print("-1")