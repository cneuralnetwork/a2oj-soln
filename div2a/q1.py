from operator import xor
import math
 
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
    s=input()
    ns,rs=0,0
    for i in s:
        if i=='n':
            ns+=1
        elif i=='r':
            rs+=1
    ans=[]
    for i in range(ns):
        ans.append('1')
    for i in range(rs):
        ans.append('0')
    print(' '.join(ans))