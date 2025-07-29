
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

a = [int(input()) for _ in range(n)]

count = 0

for coin in reversed(a):
    if k >= coin:
        count += k // coin
        k %= coin

print(count)
