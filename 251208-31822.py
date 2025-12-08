
code = input()

n = int(input())

count = 0
for _ in range(n):
    sub = input()
    if code[:5] == sub[:5]:
        count += 1

print(count)