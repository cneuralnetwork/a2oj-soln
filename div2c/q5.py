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
    arr.sort()
    ans = [0] * n
    left, right = 0, n - 1
    for i in range(n):
        if i % 2 == 0:
            ans[left] = arr[i]
            left += 1
        else:
            ans[right] = arr[i]
            right -= 1
    print(*ans)