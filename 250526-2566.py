
max_value = -1
row = 0
col = 0

for i in range(9):
    num = list(map(int, input().split()))
    idx = 0
    for val in num:
        idx += 1
        if val > max_value:
            max_value = val
            row = i + 1
            col = idx

print(max_value)
print(row, col)