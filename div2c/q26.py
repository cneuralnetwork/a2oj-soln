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
    if n==1:
        print(-1)
    else:
        print(n,n+1,n*(n+1))