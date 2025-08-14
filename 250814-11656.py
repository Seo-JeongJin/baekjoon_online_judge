
from collections import deque

txt = input()

q = deque(txt)

lst = []

for _ in range(len(q)):
    lst.append("".join(q))
    q.popleft()

lst.sort()

for value in lst:
    print(value)