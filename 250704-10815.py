
n = int(input())

nums = set(map(int, input().split()))

m = int(input())

in_cards = list(map(int, input().split()))

for card in in_cards:
    print(1 if card in nums else 0, end=" ")
