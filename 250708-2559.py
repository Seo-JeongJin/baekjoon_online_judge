# sliding window
# test case
# input
# 10 2
# 3 -2 -4 -9 0 3 7 13 8 -3

# 해설)
# k = 3 일 때, 
# 3 -2 -4
# 다음 윈도우로 넘어가면
#   -2 -4 -9
# -> [-2, -4] 라는 중복되는 부분이 생김
# 이런 식으로 슬라이딩 윈도우에서는,
# 1. 먼저 k개의 합을 구해 놓고, 
# 2. 다음 윈도우로 이동할 때
# - 가장 앞의 값을 빼고, 
# - 새로 들어오는 값을 더해주면 다음 구간의 합을 계산할 수 있다
# 첫 번째 구간의 합 : 3 + (-2) + (-4) = -3
# 그 다음 구간의 합은 이전 합 (-3)에서 가장 앞의 값(3)을 빼고
# 새로 들어오는 값(-9)을 더하면 된다
# 즉, -3 - 3 + (-9) = -15


n, k = map(int, input().split())

arr = list(map(int, input().split()))

window_sliding = sum(arr[:k])
max_value = window_sliding

for i in range(k, n):
    window_sliding += arr[i] - arr[i-k]
    max_value = max(max_value, window_sliding)

print(max_value)