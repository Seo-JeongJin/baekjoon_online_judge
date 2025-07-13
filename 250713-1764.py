
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

set_n = set()
set_m = set()

for _ in range(n):
    name = input().strip()
    set_n.add(name)

for _ in range(m):
    name = input().strip()
    set_m.add(name)

result = sorted(set_n & set_m)

print(len(result))
for name in result:
    print(name)
