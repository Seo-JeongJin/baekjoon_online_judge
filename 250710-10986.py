
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int, input().split()))
S = [0] * n

# m을 곱해주는 이유
# m=3 일 때, 나머지는 [0, 1, 2] 3가지가 나오기 때문
# 0, 1, 2 가 나온 횟수를 구하기 위한 count임
count = [0] * m
result = 0

S[0] = A[0]

for i in range(1, n):
    S[i] = S[i-1] + A[i]
    
for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        result += 1
    count[remainder] += 1

for i in range(m):
    # 나머지가 나온 횟수가 2개 이상일 때
    if count[i] > 1:
        # 같은 나머지를 가진 누적합 두 개를 찾으면 그 사이 구간합은 m의 배수 
        # n개중 아무거나 2개 뽑기 nC2
        result += (count[i] * (count[i]-1) // 2)
        
print(count)
print(result)