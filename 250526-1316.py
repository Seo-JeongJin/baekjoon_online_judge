
n = int(input())

count = 0

for _ in range(n):
    word = input()
    used = []
    prev_char = ""
    is_group = True
    
    for char in word:
        if char != prev_char:
            if char in used:
                is_group = False
                break
            used.append(char)
        prev_char = char
    
    if is_group:
        count += 1
        
print(count)