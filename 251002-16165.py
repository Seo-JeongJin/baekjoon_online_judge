
n, m = map(int, input().split())

dic = {}

for _ in range(n):
    group = input()
    num = int(input())
    for _ in range(num):
        member = input()
        if group not in dic:
            dic[group] = []
        dic[group].append(member)
        
for _ in range(m):
    name = input()
    quiz = int(input())
    if quiz == 1:
        for g, m in dic.items():
            if name in m:
                print(g)
                break
    else:
        # dic[name].sort()
        for mem in sorted(dic[name]):
            print(mem)