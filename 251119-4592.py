
while True:
    a = list(map(int, input().split()))
    if a[0] == 0:
        break

    prev = None
    for x in a[1:]:
        if x != prev:
            print(x, end=' ')
        prev = x
    print('$')