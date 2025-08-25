
n, m = map(int, input().split())

dic = {}
for _ in range(n):
    value = input().split()
    dic[value[0]] = value[1]

for _ in range(m):
    site = input()
    print(dic[site])
