
# 소수(Prime Number) : 1보다 큰 자연수 중에서 1과 자기 자신만을 약수로 가지는 수

n = int(input())

numbers = list(map(int, input().split()))

count = 0
for num in numbers:
    if num < 2: # 0, 1은 소수가 아니기 때문에 넘어감
        continue

    for i in range(2, num): 
        if num % i == 0: # numbers 안의 요소가 자기 자신을 제외한 숫자에서 나누어 떨어질 때 소수가 아님을 판별
            break
        
    else: # for-else : for루프가 끝나면 else 실행, for 중간에 break 걸리면 else는 실행 안됨
        count += 1
        
print(count)