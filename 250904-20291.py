
n = int(input())

dic = {}

for _ in range(n):
    file = input().split(".")
    if file[1] not in dic:
        dic[file[1]] = 0
    dic[file[1]] += 1

for k, v in sorted(dic.items()):
    print(k, v)