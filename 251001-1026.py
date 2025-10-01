
n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

min_value = 0
for i in range(n):
    min_value += a[i] * b[i]
    
print(min_value)