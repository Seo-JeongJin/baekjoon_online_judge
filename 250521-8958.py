
t = int(input())

for _ in range(t):
    o_x = input()
    count = 0
    num_list = []
    for char in o_x:
        if char == "O":
            count += 1
        elif char == "X":
            count = 0
        num_list.append(count)
    print(sum(num_list))