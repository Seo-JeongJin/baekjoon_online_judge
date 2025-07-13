
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

# & == 집합(set) 자료형에서 교집합 연산자로 사용 가능
result = sorted(set_n & set_m)

print(len(result))
for name in result:
    print(name)
