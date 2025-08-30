
score = []
for _ in range(5):
    lst = list(map(int, input().split()))
    score.append(sum(lst))
    
max_value = max(score)

print(score.index(max_value)+1, max_value)
