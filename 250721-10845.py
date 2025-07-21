
from collections import deque
import sys
input = sys.stdin.readline

queue = deque()

n = int(input())

for _ in range(n):
    values = input().split()
    if values[0] == "push":
        queue.append(int(values[1]))
    elif values[0] == "pop":
        print(queue.popleft() if queue else -1)
    elif values[0] == "size":
        print(len(queue))
    elif values[0] == "empty":
        print(0 if queue else 1)
    elif values[0] == "front":
        print(queue[0] if queue else -1)
    else:
        print(queue[-1] if queue else -1)
