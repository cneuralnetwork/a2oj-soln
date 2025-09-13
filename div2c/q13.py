import sys
from collections import deque,defaultdict

def inp():
    return int(sys.stdin.readline())
def inlt():
    return list(map(int, sys.stdin.readline().split()))
def insr():
    s = sys.stdin.readline()
    return list(s[:len(s) - 1])
def invr():
    return map(int, sys.stdin.readline().split())
def invr_str():
    return sys.stdin.readline().split()

t = 1
for _ in range(t):
    n=inp()
    book=defaultdict(set)
    for i in range(n):
        parts=invr_str()
        book[parts[0]].add(parts[2:])
    