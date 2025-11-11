
c = int(input())  
n = 1
x = c

while x != 1:
    if x % 2 == 0:
        x //= 2
    else:
        x = 3 * x + 1
    n += 1

print(n)
