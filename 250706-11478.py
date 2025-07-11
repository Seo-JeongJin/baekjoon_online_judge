
import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    x, y = map(int, input().split())
    coor = x, y
    graph.append(coor)
    
graph.sort()

for srted in graph:
    print(*srted)
