n=int(input())
ans=[0]*n
A=list(map(int,input().split()))
mStack=[] 
for i in range(n):
  while mStack and A[mStack[-1]]<A[i]:
    ans[mStack.pop()]=A[i]
  mStack.append(i)
while mStack:
  ans[mStack.pop()]=-1
for i in range(n):
  print(ans[i],end=' ')
