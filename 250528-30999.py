
n, m = map(int, input().split())

count = 0
for _ in range(n):
    o_x = input()
    o_x_list = []
    for char in o_x:
        o_x_list.append(char)
    if o_x_list.count("O") > o_x_list.count("X"):
        count += 1

print(count)