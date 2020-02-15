import operator as op
from functools import reduce
    
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom
    
t=int(input())
for i in range(t):
    n,k = map(int,input().split())
    if(n==k):
        ans=1
    else:
        ans=ncr(n-1,k-1)
    a=(int)(ans)
    print(a)
