
n = int(input())

nums = set(map(int,input().split()))

m = int(input())

in_a = list(map(int, input().split()))

for a in in_a:
    print(1 if a in nums else 0)