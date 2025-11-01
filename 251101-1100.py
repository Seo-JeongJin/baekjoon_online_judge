
count = 0

for i in range(8):
    line = input()
    for j in range(8):
        if line[j] == "F" and (i+j)%2 == 0:
            count += 1

print(count)