
n = list(map(int, input().split()))

s = sorted(n)

print("Good" if n == s else "Bad")