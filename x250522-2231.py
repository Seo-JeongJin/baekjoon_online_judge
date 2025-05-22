
n = input()

sum_list = []
for char in n:
    sum_list.append(char)
    
sum_list = list(map(int, sum_list))

print(int(n) + sum(sum_list))