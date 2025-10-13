
t = int(input())

for _ in range(t):
    scores = list(map(int, input().split()))
    scores.sort()
    
    middle = scores[1:4]
    if middle[2] - middle[0] >= 4:
        print("KIN")
    else:
        print(sum(middle))
