
n = int(input())

for _ in range(n):
    num = int(input())
    print(f"{num} is even" if num % 2 == 0 else f"{num} is odd")