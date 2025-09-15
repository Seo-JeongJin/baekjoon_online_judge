
n = int(input())

names = input().split()
dic = dict.fromkeys(names, 0)

for _ in range(n):
    infos = input().split()
    for info in infos:
        dic[info] += 1
    
for k, v in sorted(dic.items(), key=lambda x:x[1], reverse=True):
    print(k, v)