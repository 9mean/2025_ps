from queue import PriorityQueue
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x]==x:
        return x
    
    parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a

v,e=map(int,input().split())
pq=PriorityQueue()
parent=[0]*(v+1)
for i in range(v+1):
    parent[i]=i

for _ in range(e):
    a,b,c=map(int,input().split())
    pq.put((c,a,b))

cnt=0
res=0
while cnt<v-1:
    c,a,b=pq.get()
    a=find(a)
    b=find(b)
    if a!=b:
        union(a,b)
        res+=c
        cnt+=1
print(res)
