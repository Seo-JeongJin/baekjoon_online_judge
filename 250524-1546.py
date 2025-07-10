
N = int(input())

score = list(map(int, input().split()))

m = 0
val_list = []
for val in score:
    val_list.append(val)
    if val > m:
        m = val

converted_list = []
for val in val_list:
    val = val / m * 100
    converted_list.append(val)

print(sum(converted_list) / N)
