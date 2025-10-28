
t = int(input())

for _ in range(t):
    n = int(input())
    total_credit = 0
    total_score = 0.0
    
    for _ in range(n):
        c, g = input().split()
        c = int(c)
        g = float(g)
        total_credit += c
        total_score += c * g
    
    print(total_credit, total_score / total_credit)
