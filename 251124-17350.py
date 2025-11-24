
n = int(input())
found = False

for _ in range(n):
    member = input()
    if member == "anj":
        found = True
        break

if found:
    print("뭐야;")
else:
    print("뭐야?")