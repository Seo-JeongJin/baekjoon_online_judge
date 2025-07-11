
w = [int(input()) for _ in range(10)]
k = [int(input()) for _ in range(10)]

w.sort()
k.sort()

print(sum(w[::-1][0:3]), sum(k[::-1][0:3]))