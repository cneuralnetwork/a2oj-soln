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
    n=inp()
    spf=[0]*(n+1)
    prime_idx={}
    idx=1
    for i in range(2,n+1):
        if spf[i]==0:
            spf[i]=i
            prime_idx[i]=idx
            idx+=1
        for j in range(2,n//i+1):
            if spf[i*j] == 0:
                spf[i*j] = i
    ans=[]
    for i in range(2,n+1):
        p=spf[i]
        ans.append(str(prime_idx[p]))
    print(*ans)
    