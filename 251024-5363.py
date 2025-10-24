
n = int(input())

for _ in range(n):
    txt = input().split()
    txt.append(txt[0])
    txt.append(txt[1])
    del txt[0]
    del txt[0]
    print(*txt)
    
