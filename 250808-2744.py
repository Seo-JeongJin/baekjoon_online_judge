
txt = input()

answer = ""

for char in txt:
    if char.islower():
        answer += char.upper()
    else:
        answer += char.lower()

print(answer)
