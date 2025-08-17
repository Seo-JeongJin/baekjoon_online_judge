
k = int(input())

for i in range(k):
    score = list(map(int, input().split()))
    max_score = max(score[1:])
    min_score = min(score[1:])
    
    scores = score[1:]
    
    scores.sort(reverse=True)
    
    largest_gap = 0
    for j in range(len(scores)-1):
        gap = scores[j] - scores[j+1]
        if gap > largest_gap:
            largest_gap = gap
            
    print(f"Class {i+1}\nMax {max_score}, Min {min_score}, Largest gap {largest_gap}")
