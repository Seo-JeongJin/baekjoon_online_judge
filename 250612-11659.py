
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

prefix_sum = [0]
temp = 0

for val in nums:
    temp += val
    prefix_sum.append(temp)
    
for _ in range(m):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])