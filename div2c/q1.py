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
    arr=inlt()
    s=0
    arr=sorted(arr,reverse=False)
    for i in range(n//2):
        s+=(arr[i]+arr[n-i-1])**2

    print(s)