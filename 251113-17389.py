
n = int(input())

ox = input()

bonus = 0
score = 0
for i in range(n):
    if ox[i] == "X":
        bonus = 0
    else:
        score += i+1+bonus
        bonus += 1

print(score)