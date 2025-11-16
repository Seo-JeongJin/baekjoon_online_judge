
n = int(input())

s = list(map(int, input().split()))

mst = 0
st = 0
for num in s:
    if num >= 1:
        st += 1
    else:
        st = 0
    if st > mst:
        mst = st

print(mst)