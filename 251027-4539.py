
n = int(input())
for _ in range(n):
    x = int(input())
    place = 10
    while x >= place:
        x = ((x + place//2) // place) * place
        place *= 10
    print(x)