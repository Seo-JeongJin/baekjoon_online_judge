
while True:
    num = input()
    if num == "0":
        break
    
    while len(num) > 1:
        s = 0
        for char in num:
            s += int(char)
        num = str(s)
        
    print(num)