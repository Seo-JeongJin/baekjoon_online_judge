
import sys

n = int(sys.stdin.readline())
c, s = 100, 100  

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a < b:
        c -= b
    elif a > b:
        s -= a

print(c)
print(s)
