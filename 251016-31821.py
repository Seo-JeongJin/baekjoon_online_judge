
n = int(input())
menu = [int(input()) for _ in range(n)]

m = int(input())
total = 0
for _ in range(m):
    idx = int(input())
    total += menu[idx-1]

print(total)