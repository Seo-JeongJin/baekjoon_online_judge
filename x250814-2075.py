
import sys
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    nums = list(map(int, input().split()))
    for num in nums:
        arr.append(num)

arr.sort()
   
print(arr[-n])