from operator import xor
import math
import collections
 
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

t=1
for _ in range(t):
    n,k=invr()
    before=inlt()
    after=inlt()
    paired = list(zip(before, after))
    paired.sort(key=lambda x: x[0] - x[1])
    ans=0
    for idx,(i,j) in enumerate(paired):
        if k!=0:
            ans+=i
            k-=1
        else:
            ans+=min(i,j)
    print(ans)

    