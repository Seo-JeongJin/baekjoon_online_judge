
num_list = []
for i in range(9):
    n = int(input())
    num_list.append(n)
    
max_value = 0
count = 0

for element in num_list:
    count += 1
    if element > max_value:
        max_value = element
        idx = count
        
print(f"{max_value}\n{idx}")
# print(f"{max_value}\n{num_list.index(max_value) + 1}")도 가능