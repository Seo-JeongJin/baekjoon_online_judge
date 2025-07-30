
t = int(input())

for _ in range(t):
    values = input()
    count = 0
    valid = True
    for value in values:
        if value == "(":
            count += 1
        else:
            count -= 1
            # count가 0보다 작아진다는 것은 닫는 괄호가 먼저 나왔다는 뜻으로
            # VPS가 아님
            if count < 0:
                valid = False
    # 루프를 다 돌았는데도 count가 0이 아니라면
    # 여는 괄호가 남았다는 뜻이므로 VPS가 아님
    if count != 0:
        valid = False
    print("YES" if valid else "NO")
