
n = int(input())

seats = input()

s_cnt, l_cnt = 0, 0

for seat in seats:
    if seat == "S":
        s_cnt += 1
    else:
        l_cnt += 1
    
if l_cnt == 0:
    print(n)
elif s_cnt == 0:
    print(n-1)
else:
    print(s_cnt+(l_cnt//2)+1)
