
import sys
input = sys.stdin.readline

n = int(input())

num_list = []
for _ in range(n):
    t = int(input())
    num_list.append(t)

num_list.sort()
for val in num_list:
    print(val)

# for i in range(n):
#     for j in range(0, n - i - 1):  # 뒤에 i개는 이미 정렬돼 있음
#         if num_list[j] > num_list[j + 1]:
#             num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]  # swap

# for val in num_list:
#     print(val)
