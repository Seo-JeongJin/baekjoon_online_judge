
import sys
input = sys.stdin.readline

N = int(input().strip())
count = {"STRAWBERRY": 0, "BANANA": 0, "LIME": 0, "PLUM": 0}

for _ in range(N):
    S, X = input().split()
    count[S] += int(X)

print("YES" if any(v == 5 for v in count.values()) else "NO")
