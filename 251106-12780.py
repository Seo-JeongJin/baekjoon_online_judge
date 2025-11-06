
def count_occurrences(h, n):
    count = 0
    i = 0
    while True:
        index = h.find(n, i)  # i부터 검색
        if index == -1:       # 더 이상 없으면 종료
            break
        count += 1
        i = index + len(n)    # 겹치지 않게 다음 위치로 이동
    return count



h = input()
n = input()

print(count_occurrences(h, n))
