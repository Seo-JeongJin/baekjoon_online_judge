import sys
input = sys.stdin.readline

n = int(input())

dic = {}

for _ in range(n):
    age, name = input().split()
    age = int(age)
    if age in dic:
        dic[age] += [name]
    else:
        dic[age] = [name]

for age, names in sorted(dic.items()):
    for name in names:
        print(*(age, name))