
t = int(input())

for _ in range(t):
    val = input().split()
    if val[1] == "+":
        result = int(val[0]) + int(val[2])
    elif val[1] == "-":
        result = int(val[0]) - int(val[2])
    elif val[1] == "*":
        result = int(val[0]) * int(val[2])
    else:
        result = int(val[0]) / int(val[2])
        
    if result == int(val[4]):
        print("correct")
    else:
        print("wrong answer")