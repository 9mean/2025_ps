from queue import PriorityQueue
import sys
#10만개 이상 입력받을때는 sys.stdin.readline()사용
#input()은 시간초과남
input=sys.stdin.readline

V,E=map(int,input().split())
k=int(input())
INF=123456789
distance=[INF]* (V+1)
distance[k]=0
visited=[False]*(V+1)
node=[[] for _ in range(V+1)]
q=PriorityQueue()
q.put((0,k))
for i in range(E):
    u,v,w=map(int,input().split())
    node[u].append((v,w))

while q.qsize()>0:
    dist,now=q.get()
    if visited[now]:
        continue
    visited[now]=True
    for x in node[now]:
        cost=distance[now]+x[1]
        if cost<distance[x[0]]:
            distance[x[0]]=cost
            q.put((cost,x[0]))
            

for i in range(1,V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF") 
