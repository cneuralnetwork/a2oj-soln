from operator import xor
import math

def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def insr():
    s = input()
    return list(s[:len(s) - 1])
def invr():
    return map(int, input().split())

t = 1
for _ in range(t):
    n, m = invr()
    s = list(input())
    for _ in range(m):
        l, r, c1, c2 = input().split()
        l = int(l)
        r = int(r)
        for i in range(l - 1, r):
            if s[i] == c1:
                s[i] = c2
    print(''.join(s))