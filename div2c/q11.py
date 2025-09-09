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
    k,a,b=invr()
    x=a//k
    y=b//k
    n=x+y
    if n==0:
        print(-1)
    else:
        A=a-x*k
        B=b-y*k
        ok=1
        if not(0<=A<=y*(k-1)):
            ok=0
        if not(0<=B<=x*(k-1)):
            ok=0
        if ok:
            print(n)
        else:
            print(-1)