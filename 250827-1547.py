
m = int(input())

lst = [1, 0, 0]

for _ in range(m):
    x, y = map(int, input().split())
    lst[x-1], lst[y-1] = lst[y-1], lst[x-1]

print(lst.index(1)+1)
