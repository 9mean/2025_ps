n=int(input())
paper=[[0]*100 for _ in range(100)]
for i in range(n):
  x,y=map(int,input().split())
  for j in range(x,x+10):
    for k in range(y,y+10):
      if paper[j][k]==0:
        paper[j][k]=1
res=0
for i in range(100):
  res+=sum(paper[i])
print(res)