
N, M = map(int, input().split())
for _ in range(N):
    row = list(input().strip())
    left = row[:M//2]
    right = row[M//2:][::-1]
    for i in range(M//2):
        if left[i] == '.' and right[i] != '.':
            left[i] = right[i]
        if right[i] == '.' and left[i] != '.':
            right[i] = left[i]
    print(''.join(left + right[::-1]))
