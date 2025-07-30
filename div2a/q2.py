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
    n=inp()
    s=input()
    sf,fs=0,0
    if n==2:
        if s[0]=='S' and s[1]=='F':
            sf+=1
        elif s[0]=='F' and s[1]=='S':
            fs+=1
    for i in range(n-1):
        if s[i]=='S' and s[i+1]=='F':
            sf+=1
        elif s[i]=='F' and s[i+1]=='S':
            fs+=1
    # print(sf,fs)
    if sf>fs:
        print("YES")
    else:
        print("NO")