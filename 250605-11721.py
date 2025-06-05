
string = input()

count = 0
word = ""
for char in string:
    count += 1
    word += char
    if count % 10 == 0:
        print(word)
        word = ""
print(word)