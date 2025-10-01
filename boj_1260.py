from collections import deque
def dfs(start):
    visited=[0]*(n+1)
    stack=[start]
    while stack:
        node=stack.pop()
        if not visited[node]:
            visited[node]=1
            print(node,end=' ')
            for neighbor in v[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)
def bfs(start):
    visited=[0]*(n+1)
    queue=deque([start])
    while queue:
        node=queue.popleft()
        if not visited[node]:
          
            visited[node]=1
            print(node,end=' ')
            for neighbor in qv[node]:
                if not visited[neighbor] and neighbor not in queue:
                    queue.append(neighbor)
                  

n,m,start=map(int,input().split())
v=[[] for _ in range(n+1)]
qv=[[] for _ in range(n+1)]
for _ in range(m):
  a,b=map(int,input().split())
  v[a].append(b)
  v[b].append(a)
  v[a].sort(reverse=True)
  v[b].sort(reverse=True)
  qv[a].append(b)
  qv[b].append(a)
  qv[a].sort()
  qv[b].sort()

dfs(start)
print()
bfs(start)