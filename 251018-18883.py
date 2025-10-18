
n, m = map(int, input().split())

idx = 1
for _ in range(n):
    for j in range(m):
        if j != m-1:
            print(idx, end=" ")
        else:
            print(idx)
        idx += 1