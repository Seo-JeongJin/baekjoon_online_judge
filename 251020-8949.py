
a, b = input().split()

max_len = max(len(a), len(b))
a = a.zfill(max_len)
b = b.zfill(max_len)

result = ""

for i in range(max_len):
    total = int(a[i]) + int(b[i])
    result += str(total)

print(result)