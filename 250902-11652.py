
import sys
input = sys.stdin.readline

n = int(input())

dic = {}

for _ in range(n):
    value = int(input())
    if value not in dic:
        dic[value] = 0
    dic[value] += 1

max_value = max(dic.values())

max_keys = []

for k, v in dic.items():
    if v == max_value:
        max_keys.append(k)

print(min(max_keys))