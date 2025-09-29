def gcb(a,b):
    while b:
        a,b=b,a%b
    return a

t=int(input())
for _ in range(t): 
    a,b=map(int,input().split())
    print(int(a*b//gcb(a,b)))