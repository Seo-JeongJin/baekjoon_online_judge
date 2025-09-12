
t = int(input())

for _ in range(t):
    num = input()
    rev_num = num[::-1]    
    total = int(num) + int(rev_num)
    print("YES" if str(total) == str(total)[::-1] else "NO")

