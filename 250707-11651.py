
import sys
input = sys.stdin.readline

graph = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    coord = x, y
    coord = list(coord)
    graph.append(coord)

for i in range(len(graph)):
    graph[i] = graph[i][::-1]

graph.sort()

for i in range(len(graph)):
    graph[i] = graph[i][::-1]

for coord in graph:
    print(*coord)
