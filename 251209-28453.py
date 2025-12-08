
n = int(input())

lvl = list(map(int, input().split()))

lst = []
for l in lvl:
    if l == 300:
        lst.append(1)
    elif l >= 275:
        lst.append(2)
    elif l >= 250:
        lst.append(3)
    else:
        lst.append(4)

print(*lst)