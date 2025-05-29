
n, m = map(int, input().split())

num_list = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    num_list[i-1:j] = num_list[i-1:j][::-1]

for val in num_list:
    print(val, end=" ")