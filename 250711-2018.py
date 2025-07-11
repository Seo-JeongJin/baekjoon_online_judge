
n = int(input())

# while end != n == end가 n이 아닌 동안만 반복
# 자기 자신을 세는 것으로 count = 1로 초기화
count = 1
start = 1
end = 1
total = 1

while end != n:
    if total == n:
        # 같으면 카운트
        count += 1
        # start를 늘리면 total 값을 빼줘야 하니 당연히 아니고
        # end를 늘려서 자연수 범위 확장
        end += 1
        # end 늘면 당연히 total 에 end 값 추가
        total += end
    elif total > n:
        # total이 더 크면 end를 움직였을 때 당연히 수가 더 커지기만 하므로 end는 x
        # start 값을 total 에서 빼고
        total -= start
        # start 값을 움직임
        start += 1
    else:
        # total이 n보다 작아지면 자연수 값 확장
        end += 1
        # end값을 total에 추가
        total += end

print(count)
