
from collections import deque

n = int(input())

q = deque(range(1, n+1))

lst = []

while q:
    lst.append(q.popleft())
    if q:
        q.append(q.popleft())

print(*lst)
    
    