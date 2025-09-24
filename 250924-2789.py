
email = input()

cam = ["C", "A", "M", "B", "R", "I", "D", "G", "E"]

result = ""
for char in email:
    if char not in cam:
        result += char
    
print(result)