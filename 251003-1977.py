m = int(input())
n = int(input())

lst = []
for i in range(int(m**(1/2)), int(n**(1/2))+1):
    sq = i**2
    if m <= sq <= n:
        lst.append(sq)

print(f"{sum(lst)}\n{min(lst)}" if lst else -1)
