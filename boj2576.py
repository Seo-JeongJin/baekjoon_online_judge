
nums = [int(input()) for _ in range(7)]

odd = []
even = []

for num in nums:
    even.append(num) if num % 2 == 0 else odd.append(num)
    
print(-1 if len(even) == 7 else f"{sum(odd)}\n{min(odd)}")

"""

조금 더 깔끔히 풀이
nums = [int(input()) for _ in range(7)]
odd = [num for num in nums if num % 2] # if num % 2 -> 0 일때 False, 그 외 숫자 True
print(-1 if len(odd) == 0 else f"{sum(odd)}\n{min(odd)}")

"""
