
a = int(input())
b = int(input())
c = int(input())

lst = [0]*10

mul = str(a*b*c)

for num in mul:
    lst[int(num)] += 1

for num in lst:
    print(num)