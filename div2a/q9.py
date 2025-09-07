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

t=1
for _ in range(t):
    n = inp()
    cols = []
    for _ in range(n):
        s = insr()
        cols.append(s[0])
    mp = {"r":"Reality","y":"Mind","b":"Space","g":"Time","o":"Soul","p":"Power"}
    all_colors = set(mp.keys())
    present = set(cols)
    missing = all_colors - present
    print(len(missing))
    for c in missing:
        print(mp[c])