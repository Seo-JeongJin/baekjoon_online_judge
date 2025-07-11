
a, b, v = map(int, input().split())

distance = a - b
s = 0
count = 0

while True:
    count += 1
    s += a
    if s >= v:
        break
    s -= distance

print(count)
