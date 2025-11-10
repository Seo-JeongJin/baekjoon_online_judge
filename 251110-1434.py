

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

used = [0] * N

for book in B:
    for i in range(N):
        if used[i] + book <= A[i]:
            used[i] += book
            break

wasted = sum(A[i] - used[i] for i in range(N))
print(wasted)
