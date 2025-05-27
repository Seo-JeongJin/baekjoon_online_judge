
text = input().upper()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
freq = [0] * 26

for char in text:
    for i in range(26):
        if char == alphabet[i]:
            freq[i] += 1
            break

max_value = -1
for val in freq:
    if val > max_value:
        max_value = val
        
max_count = 0
for val in freq:
    if val == max_value:
        max_count += 1

if max_count > 1:
    print("?")
    
else:
    for i in range(26):
        if freq[i] == max_value:
            print(alphabet[i])
            break