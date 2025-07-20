
from collections import deque

n, k = map(int, input().split())

people = deque(range(1, n+1))
arr = []

# people에 요소가 있는 동안 반복
while people:
    # 동작 예
    # people == [1, 2, 3, 4, 5, 6, 7] 
    # -> [3, 4, 5, 6, 7, 1, 2] people의 가장 왼쪽에 있는 요소 k-1개를 
    # 제거 후 people에 append
    # -> [4, 5, 6, 7, 1, 2] people의 가장 왼쪽 요소 제거 후
    # arr == [3] # arr에 append
    # 이 과정을 people에 요소가 없어질 때까지 반복
    for _ in range(k-1):
        people.append(people.popleft())
    arr.append(people.popleft())

# .join() == 문자열 리스트(또는 iterable)를 하나의 문자열로 연결하는 메서드
# arr의 문자열 요소들을 ", "로 연결시켜주는 메서드임
print("<"+", ".join(map(str, arr))+">")
