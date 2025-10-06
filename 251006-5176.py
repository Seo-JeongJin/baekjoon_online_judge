
import sys
input = sys.stdin.readline

k = int(input())

for _ in range(k):
    p, m = map(int, input().split())
    dic = {i+1 : 0 for i in range(m)}
    count = 0
    for _ in range(p):
        seat = int(input())
        if dic[seat] == 0:
            dic[seat] = 1
        else:
            count += 1
    print(count)