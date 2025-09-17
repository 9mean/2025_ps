n=int(input())
p=list(map(int,input().split()))
p.sort()
res=0
k=0
for i in range(n):
  k+=p[i]
  res+=k
print(res)