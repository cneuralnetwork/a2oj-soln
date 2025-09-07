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
    s=input()
    if n%2==1:
        print("No")
        continue
    if s.count('(')!=s.count(')'):
        print("No")
        continue
    b,m=0,0
    for ch in s:
        b+=1 if ch=='(' else -1
        m=min(m,b)
    if m>=-1:
        print("Yes")
    else:
        print("No")