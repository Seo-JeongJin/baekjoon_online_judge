
n, m = map(int, input().split())

basket = [0 for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    basket[i-1:j] = [k] * (j - i + 1)

print(*basket)