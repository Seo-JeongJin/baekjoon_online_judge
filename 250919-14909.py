
arr = input().split()

count = 0
for val in arr:
    if val[0] != "-" and val[0] != "0":
        count += 1
        
print(count) 