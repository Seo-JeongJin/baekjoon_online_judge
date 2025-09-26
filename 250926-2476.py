
n = int(input())

prize = []
for _ in range(n):
    dice = list(map(int ,input().split()))
    dice.sort()
    if dice[0] == dice[1] == dice[2]:
        prize.append(10000+(dice[0]*1000))
    elif dice[0] == dice[1] or dice[1] == dice[2]:
        prize.append(1000+(dice[1]*100))
    else:
        prize.append(max(dice)*100)

print(max(prize))