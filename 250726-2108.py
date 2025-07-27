from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())

lst = [int(input()) for _ in range(n)]

# 산술평균 (소수 첫째 자리에서 반올림)
print(round(sum(lst)/n))

# 중앙값
lst.sort()
print(lst[n // 2])

# 최빈값
count = Counter(lst)
max_count = max(count.values())
freq = []
for num in count:
    if count[num] == max_count:
        freq.append(num)
freq.sort()
if len(freq) > 1:
    print(freq[1])  # 두 번째로 작은 값
else:
    print(freq[0])

# 범위
print(max(lst) - min(lst))
