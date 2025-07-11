
n, m = map(int, input().split())

st = set()
for _ in range(n):
    s = input()
    st.add(s)

lst = []
for _ in range(m):
    check = input()
    lst.append(check)

cnt = 0
for string in lst:
    if string in st:
        cnt += 1

print(cnt)
