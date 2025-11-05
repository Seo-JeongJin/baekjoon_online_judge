
n = int(input())

for _ in range(n):
    text = input()
    lower_text = text.lower()
    print("Yes" if lower_text == lower_text[::-1] else "No")
