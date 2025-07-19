
import sys
input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    num = list(map(int, input().split()))
    if num[0] == 1:
        stack.append(num[1])
    elif num[0] == 2:
        print(stack.pop() if stack else -1)
    elif num[0] == 3:
        print(len(stack))
    elif num[0] == 4:
        print(1 if not stack else 0)
    else:
        print(stack[-1] if stack else -1)
