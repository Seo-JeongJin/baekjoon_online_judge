
n, m = map(int, input().split())

num_list = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    num_list[i - 1], num_list[j - 1] = num_list[j - 1], num_list[i - 1]

print(*num_list)