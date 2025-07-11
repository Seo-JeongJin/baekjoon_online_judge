
n, m = map(int, input().split())

card = list(map(int, input().split()))

max_sum = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            total = card[i] + card[j] + card[k]
            if total <= m and max_sum < total:
                max_sum = total
                
print(max_sum)