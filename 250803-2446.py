
n = int(input())

for i in range(n):
    print(" " * i + "*" * (n*2-1-(i*2)))
for i in range(n-1):
    print(" " * (n-2-i) + "*" * (3+(i*2)))
