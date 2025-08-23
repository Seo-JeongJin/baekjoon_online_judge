
n = int(input())

arr = list(map(int, input().split()))

count = 0
score = 0
for result in arr:
    if result == 1:
        score += 1
        count += score
    else:
        score = 0
        
print(count)
