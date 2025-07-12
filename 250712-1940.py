import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
lst = list(map(int, input().split()))

# 작은 수부터 비교 가능해야하니 정렬 필수
lst.sort()

# 리스트의 맨 앞
start = 0
# 리스트의 맨 뒤
end = n-1
count = 0

# start는 커지기만 하고
# end는 작아지기만 함 (생각 해보면 앎)

# start, end 투 포인터를 써서 리스트 양쪽 끝에서부터 안쪽으로 좁혀오며
# 조건을 만족하는 쌍을 찾음
# start와 end가 같은 위치에 오면, 같은 수를 두 번 더하는 셈이 되기 때문에
# start가 end보다 작을 때 까지만 반복
while start < end:
    if lst[start]+lst[end] == m:
        # 리스트 각 포인터의 합과 m이 같으므로 count 증가
        count += 1
        # 그러므로 양쪽 포인터를 이동 (생각 조금만 해보면 앎)
        start += 1
        end -= 1
    elif lst[start]+lst[end] > m:
        # 각 포인터의 합이 더 큰 상태인데 start를 올리면
        # 합이 커지기만 하므로 end -= 1 빼기
        end -= 1
    else:
        # 각 포인터의 합이 더 작은 상태인데 end를 내리면
        # 합이 작아지기만 하므로 start += 1
        start += 1

print(count)
