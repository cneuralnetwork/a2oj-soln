import sys
from collections import deque

def inp():
    return int(sys.stdin.readline())
def inlt():
    return list(map(int, sys.stdin.readline().split()))
def insr():
    s = sys.stdin.readline()
    return list(s[:len(s) - 1])
def invr():
    return map(int, sys.stdin.readline().split())

t = 1
for _ in range(t):
    n = inp()
    adj = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        u, v = invr()
        adj[u].append(v)
        adj[v].append(u)

    stack = [(1, -1)]
    res = [0.0] * (n + 1)
    visited = [False] * (n + 1)
    order = []

    while stack:
        u, p = stack.pop()
        order.append((u, p))
        for v in adj[u]:
            if v != p:
                stack.append((v, u))

    for u, p in reversed(order):
        children = [v for v in adj[u] if v != p]
        if not children:
            res[u] = 0.0
        else:
            total = 0.0
            for v in children:
                total += 1 + res[v]
            res[u] = total / len(children)

    print("{0:.15f}".format(res[1]))