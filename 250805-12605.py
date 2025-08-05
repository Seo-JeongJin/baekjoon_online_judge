
n = int(input())

for i in range(n):
    text = input().split()
    print(f"Case #{i+1}:", *text[::-1])