
n = int(input())

times = list(map(int, input().split()))

times.sort()

total = 0
lst = []
for time in times:
    total += time
    lst.append(total)

print(sum(lst))