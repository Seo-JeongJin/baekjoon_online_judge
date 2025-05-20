
a = list(map(int, input().split()))

sum = 0
for element in a:
    sum += element ** 2
    
print(sum % 10)