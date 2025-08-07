
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

count = 0
left = 0
right = 0
total = 0

while True:
    if total == m:
        count += 1
        total -= arr[left]
        left += 1
    elif total > m:
        total -= arr[left]
        left += 1
    elif right == n:
        break
    else:
        total += arr[right]
        right += 1

print(count)