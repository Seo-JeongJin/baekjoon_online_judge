
chess = [1, 1, 2, 2, 2, 8]

num = list(map(int, input().split()))

right_set = []

idx = 0
for val in chess:
    if chess[idx] - num[idx] == 0:
        right_set.append(0)
    else:
        right_set.append(chess[idx] - num[idx])
    idx += 1

for val in right_set:
    print(val, end=" ")