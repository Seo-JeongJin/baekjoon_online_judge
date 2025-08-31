import sys

vowels = set("aeiouAEIOU")

for line in sys.stdin:
    line = line.rstrip("\n")
    if line == "#":
        break
    cnt = sum(1 for ch in line if ch in vowels)
    print(cnt)
