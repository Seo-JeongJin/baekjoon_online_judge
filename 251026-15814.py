
s = list(input())

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    s[a], s[b] = s[b], s[a]

idx = 1   
for char in s:
    if idx < len(s):
        print(char, end="")
    else:
        print(char)
    idx += 1