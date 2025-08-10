
txt = input()

m = ["a", "e", "i", "o", "u"]

count = 0

for char in txt:
    if char in m:
        count += 1

print(count)
