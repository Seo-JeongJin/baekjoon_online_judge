
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

count = 0
start = 0
end = n-1

while start < end:
    if arr[start] + arr[end] > x:
        end -= 1
    elif arr[start] + arr[end] < x:
        start += 1
    else:
        count += 1
        start += 1
        end -= 1

print(count)
