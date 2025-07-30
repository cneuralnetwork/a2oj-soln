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
    s1 = input()
    s2 = input()
    s = input()
    char_map = {c1: c2 for c1, c2 in zip(s1, s2)}
    result = []
    for ch in s:
        if ch.islower():
            result.append(char_map.get(ch, ch))
        elif ch.isupper():
            lower_ch = ch.lower()
            mapped = char_map.get(lower_ch, lower_ch)
            result.append(mapped.upper())
        else:
            result.append(ch)
    print(''.join(result))
    