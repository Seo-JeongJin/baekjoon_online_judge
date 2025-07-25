
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

deq = deque()

for _ in range(n):
    values = list(map(int, input().split()))
    if values[0] == 1:
        deq.appendleft(values[1])
    elif values[0] == 2:
        deq.append(values[1])
    elif values[0] == 3:
        print(deq.popleft() if deq else -1)
    elif values[0] == 4:
        print(deq.pop() if deq else -1)
    elif values[0] == 5:
        print(len(deq))
    elif values[0] == 6:
        print(0 if deq else 1)
    elif values[0] == 7:
        print(deq[0] if deq else -1)
    else:
        print(deq[-1] if deq else -1)
