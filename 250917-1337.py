
n = int(input())

rainbow = {"ChongChong"}

for _ in range(n):
    a, b = input().split()
    if a in rainbow or b in rainbow:
        rainbow.add(a)
        rainbow.add(b)
    
print(len(rainbow))