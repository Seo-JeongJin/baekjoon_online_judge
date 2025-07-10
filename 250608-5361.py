
n = int(input())

blaster = 350.34
vision = 230.90
hearing = 190.55
arm = 125.30
leg = 180.90

for i in range(n):
    num = list(map(int, input().split()))
    print(f"${(blaster * num[0]) + (vision * num[1]) + (hearing * num[2]) + (arm * num[3]) + (leg * num[4]):.2f}")
