
b, c, d = map(int, input().split())

burger = sorted(list(map(int, input().split())))[::-1]
side = sorted(list(map(int, input().split())))[::-1]
beverage = sorted(list(map(int, input().split())))[::-1]

set_count = min(b, c, d)

discount = 0
for i in range(set_count):
    discount += (burger[i]+side[i]+beverage[i])*0.1

before = sum(burger)+sum(side)+sum(beverage)

print(before)
print(before-int(discount))