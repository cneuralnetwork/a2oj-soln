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
    n,m,k=invr()
    if m<n or k<n:
        print("NO")
    else:
        print("YES")