
import sys
input = sys.stdin.readline

m = int(input())

s = set()

for _ in range(m):
    values = input().split()
    if values[0] == "add":
        s.add(int(values[1]))
    elif values[0] == "remove":
        s.discard(int(values[1]))
    elif values[0] == "check":
        print(1 if int(values[1]) in s else 0)
    elif values[0] == "toggle":
        s.remove(int(values[1])) if int(values[1]) in s else s.add(int(values[1]))
    elif values[0] == "all":
        s = set(range(1, 21))
    elif values[0] == "empty":
        s.clear()
