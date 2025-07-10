
n = int(input())

seats = list(map(int, input().split()))

count = 0
seated = []

for seat in seats:
    if seat in seated:
        count += 1
    else:
        seated.append(seat)

print(count)
