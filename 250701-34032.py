
n = int(input())
ggs = input()

cnt1 = 0
for gg in ggs:
    if gg == "O":
        cnt1 += 1
        
print("Yes" if cnt1 >= (n+1)//2 else "No")