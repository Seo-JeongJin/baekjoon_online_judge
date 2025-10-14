
lst = []
idx = 1
val = 1
while len(lst) <= 1000:
    for _ in range(idx):
        lst.append(val)
    idx += 1
    val += 1
    
a, b = map(int, input().split())

print(sum(lst[(a-1):b]))