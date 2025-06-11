
n = int(input())

def fibo(n):
    result = []
    a, b = 1, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result[-1]

print(fibo(n))