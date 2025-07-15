
n = int(input())

total = 1
for i in range(1, n+1):
    total *= i

total = str(total)[::-1]

count = 0

for zero in total:
    if zero == "0":
        count += 1
    else:
        break

print(count)
print(total)