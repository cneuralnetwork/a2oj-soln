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
    dq=collections.deque()
    for i in range(n):
        char=s[i]
        if (n-i)%2==1:
            dq.append(char)
        else:
            dq.appendleft(char)
    print(''.join(dq))