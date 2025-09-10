lst = sorted(map(int, input().split()))

diff1 = abs((lst[0] + lst[3]) - (lst[1] + lst[2]))
diff2 = abs((lst[0] + lst[1]) - (lst[2] + lst[3]))

print(min(diff1, diff2))
