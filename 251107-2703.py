
T = int(input())

for _ in range(T):
    encrypted = input()
    rule = input()
    
    decrypt_map = {}
    for i in range(26):
        decrypt_map[rule[i]] = chr(ord('A') + i)
    
    result = ""
    for ch in encrypted:
        if ch == " ":
            result += " "
        else:
            result += decrypt_map[ch]
    
    print(result)