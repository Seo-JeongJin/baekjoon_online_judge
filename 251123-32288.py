
n = int(input())

nick = input()

result = ""
for char in nick:
    if char == "I":
        result += char.lower()
    else:
        result += char.upper()

print(result)