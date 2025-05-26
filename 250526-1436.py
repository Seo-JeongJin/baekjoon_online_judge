
import sys
input = sys.stdin.readline

n = int(input())

s = set()
for i in range(n):
    num = s.add(int(input()))

list_s = list(s)

list_s.sort()

for val in list_s:
    print(val)