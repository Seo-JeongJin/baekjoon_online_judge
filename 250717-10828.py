
import sys
input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    val = input().split()
    if val[0] == "push":
        stack.append(int(val[1]))
    elif val[0] == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif val[0] == "size":
        print(len(stack))
    elif val[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])