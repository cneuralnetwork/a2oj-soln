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
    if n%4==1 :
        print(f"0 A")
    elif n%4==2:
        print(f"1 B")
    elif n%4==3:
        print(f"2 A")
    else:
        print(f"1 A")