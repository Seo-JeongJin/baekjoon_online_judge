
t = int(input())

for _ in range(t):
    s = set()
    num = input()
    for val in num:
        s.add(val)
    print(len(s))
    