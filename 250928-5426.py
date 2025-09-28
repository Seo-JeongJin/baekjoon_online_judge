
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    txt = input()
    lst = []
    temp = int(len(txt)**(1/2))
    for i in range(temp):
        lst.append((txt[(i*temp):(temp+(i*temp))]))
    
    msg = ""
    for c in range(temp-1, -1, -1):
        for r in range(temp):
            msg += lst[r][c]
    
    print(msg)