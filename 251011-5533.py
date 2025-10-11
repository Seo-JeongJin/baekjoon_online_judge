
import sys
input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
    
result = [0]*n

for num in range(3):
    for i in range(n):
        count = 0
        for j in range(n):
            if lst[i][num] == lst[j][num]:
                count += 1
        if count == 1:
            result[i] += lst[i][num]

for val in result:
    print(val)