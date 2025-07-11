
n = int(input())

num_list = []
for i in range(n):
    num_list.append(int(input()))

for i in range(n):
    for j in range(n - i - 1):
        if num_list[j] > num_list[j + 1]:
            num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

for val in num_list:
    print(val)
