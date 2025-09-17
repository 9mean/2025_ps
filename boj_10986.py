n,m=map(int, input().split())
a=list(map(int, input().split()))
s=[0]*n
c=[0]*m
res=0
s[0]=a[0]
for i in range(1,n):
  s[i]=s[i-1]+a[i]
for i in range(n):
  reminder=s[i]%m
  if reminder==0:
    res+=1
  c[reminder]+=1
  
for i in range(m):
  if c[i]>1:
    res+=c[i]*(c[i]-1)//2

print(res)
