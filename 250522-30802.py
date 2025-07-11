
n = int(input())

applying_num_of_shirt_size = list(map(int, input().split()))

num_of_bundles = list(map(int, input().split()))

total = 0
for i in applying_num_of_shirt_size:
    total += (i + num_of_bundles[0] - 1) // num_of_bundles[0]
    
total_bundles_of_pencil = n // num_of_bundles[1]
remain_of_pencil = n % num_of_bundles[1]

print(total)
print(f"{total_bundles_of_pencil} {remain_of_pencil}")

"""
# 다른 코드
n = int(input())
applying_num_of_shirt_size = list(map(int, input().split()))
t, p = map(int, input().split())

total = 0
for i in applying_num_of_shirt_size:
    total += (i + t - 1) // t # -> 올림 계산
    
print(total)
print(f"{n // p} {n % p})
"""