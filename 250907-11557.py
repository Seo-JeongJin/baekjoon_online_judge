
n = int(input())

for _ in range(n):    
    s = int(input())
    maxL = -1
    ans = ""
    for _ in range(s):
        school, l = input().split()
        l = int(l)
        if l > maxL:
            maxL = l
            ans = school
    print(ans)    
        