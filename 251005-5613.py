
result = int(input())

while True:
    op = input()
    if op == "=":
        print(result)
        break
    num = int(input())
    
    if op == "+":
        result += num
    elif op == "-":
        result -= num
    elif op == "*":
        result *= num
    else:
        result //= num
    