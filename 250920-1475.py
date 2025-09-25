
for _ in range(3):
    n = input().strip()
    max_len = 1
    cur_len = 1
    for i in range(1, len(n)):
        if n[i] == n[i-1]:
            cur_len += 1
            max_len = max(max_len, cur_len)
        else:
            cur_len = 1
    print(max_len)

