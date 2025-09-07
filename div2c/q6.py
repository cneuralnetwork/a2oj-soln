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
    t=n*(n+1)//2
    tar=t//2
    g1=[]
    s=0
    for i in range(n,0,-1):
        if s+i<=tar:
            s+=i
            g1.append(i)
    g2=[]
    for i in range(1,n+1):
        if i not in set(g1):
            g2.append(i)
    print(abs(sum(g1)-sum(g2)))
    print(len(g1),*g1)
    