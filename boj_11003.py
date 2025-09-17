from collections import deque
n,l=map(int,input().split())
mDeque=deque()

a=list(map(int,input().split()))

for i in range(n):
  while mDeque and mDeque[-1][1]>a[i]:
    mDeque.pop()
  mDeque.append((i,a[i]))
  
  if mDeque[0][0]==i-l:
    mDeque.popleft() 
  print(mDeque[0][1],end=' ') 