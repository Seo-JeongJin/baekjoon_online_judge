
txt = input()

aeiou = ["a", "e", "i", "o", "u"
         "A", "E", "I", "O", "U"]

count = 0
for char in txt:
    if char in aeiou:
        count += 1
print(count)
