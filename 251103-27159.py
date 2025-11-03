
n = int(input())

lst = list(map(int, input().split()))

score = 0
first = lst[0]
for i in range(1, len(lst)):
    if lst[i] != lst[i-1]+1:
        score += first
        first = lst[i]

score += first
print(score)