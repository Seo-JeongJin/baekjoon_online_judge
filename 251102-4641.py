
while True:
    lst = list(map(int, input().split()))
    if lst == [-1]:
        break
    
    lst.pop()
    count = 0
    for val in lst:
        if val*2 in lst:
            count += 1
    print(count)