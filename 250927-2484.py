
n = int(input())

prize = []
for _ in range(n):
    dice = list(map(int, input().split()))
    dice.sort()
    if dice[0] == dice[1] == dice[2] == dice[3]:
        prize.append(50000+(dice[0]*5000))
    elif dice[0] == dice[1] == dice[2] or dice[1] == dice[2] == dice[3]:
        prize.append(10000+(dice[1]*1000))
    elif dice[0] == dice[1] and dice[2] == dice[3]:
        prize.append(2000+(dice[1]*500)+(dice[2]*500))
    elif dice[0] == dice[1] or dice[1] == dice[2] or dice[2] == dice[3]:
        max_value = 0
        for val in dice:
            if dice.count(val) == 2:
                max_value = val
                break
        prize.append(1000+(max_value*100))
    else:
        prize.append(max(dice)*100)
    
print(max(prize))