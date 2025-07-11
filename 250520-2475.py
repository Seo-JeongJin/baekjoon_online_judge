
# a = list(map(int, input().split()))

# sum = 0
# for element in a:
#     sum += element ** 2
    
# print(sum % 10)


# 2번째 풀이
num = list(map(int, input().split()))

for_sum_list = [element ** 2 for element in num]

print(sum(for_sum_list) % 10)