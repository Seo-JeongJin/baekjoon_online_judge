
num_list = []
for _ in range(5):
    num_list.append(int(input()))
    
num_list.sort()

print(round(sum(num_list) / 5))
print(num_list[2])

# 다른 풀이
# nums = [int(input()) for _ in range(5)]
# print(sum(nums) // 5)
# print(sorted(nums)[2])
