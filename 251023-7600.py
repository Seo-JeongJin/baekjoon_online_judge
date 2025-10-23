
while True:
    txt = input()
    
    if txt == "#":
        break
    
    s = set()
    
    for char in txt.lower():
        if char.isalpha():
           s.add(char)
    
    print(len(s)) 