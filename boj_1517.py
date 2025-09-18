def merge_sort(s,e):
  global cnt
  if e-s<1:
    return 
  m=int(s+(e-s)//2)
  merge_sort(s,m)
  merge_sort(m+1,e)
  for i in range(s,e+1):
    tmp[i]=a[i]
  
  k=s
  idx1=s
  idx2=m+1
  while idx1<=m and idx2<=e:
    if tmp[idx1]<=tmp[idx2]:
      a[k]=tmp[idx1]
      idx1+=1
    else:
      a[k]=tmp[idx2]
      cnt+=idx2-k
      idx2+=1
    k+=1
  while idx1<=m:
    a[k]=tmp[idx1]
    idx1+=1
    k+=1
  while idx2<=e:
    a[k]=tmp[idx2]
    idx2+=1
    k+=1


n=int(input())
a=list(map(int,input().split()))
a.insert(0,0)
tmp=[0]*(n+1)
cnt=0
merge_sort(1,n)
print(cnt)
