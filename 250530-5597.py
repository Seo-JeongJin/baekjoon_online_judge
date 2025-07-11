
num_list = [0 for _ in range(30)]
for _ in range(28):
    num = int(input())
    num_list[num - 1] = 1

idx = 1
for val in num_list:
    if val != 1:
        print(idx)
    idx += 1