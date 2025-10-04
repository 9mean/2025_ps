import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())
tree=[[] for _ in range(n+1)]
parent=[0]*(n+1)
for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(node):
    visited[node]=True
    
    for neighbor in tree[node]:
        if not visited[neighbor]:
            parent[neighbor]=node
            dfs(neighbor)

visited=[False]*(n+1)
dfs(1)
for i in range(2,n+1):
    print(parent[i])
