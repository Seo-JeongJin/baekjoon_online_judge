
a, b = input().split()

a_1 = int(a[::-1])
b_2 = int(b[::-1])

if a_1 > b_2:
    print(a_1)
elif a_1 < b_2:
    print(b_2)