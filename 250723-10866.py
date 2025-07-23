
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

deq = deque()

for _ in range(n):
    values = input().split()
    if values[0] == "push_front":
        deq.appendleft(values[1])
    elif values[0] == "push_back":
        deq.append(values[1])
    elif values[0] == "pop_front":
        print(deq.popleft() if deq else -1)
    elif values[0] == "pop_back":
        print(deq.pop() if deq else -1)
    elif values[0] == "size":
        print(len(deq))
    elif values[0] == "empty":
        print(0 if deq else 1)
    elif values[0] == "front":
        print(deq[0] if deq else -1)
    else:
        print(deq[-1] if deq else -1)
