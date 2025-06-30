
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

m = int(input())
nums = list(map(int, input().split()))

card_dict = {}

for card in cards:
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1

for num in nums:
    print(card_dict.get(num, 0), end=" ")

"""
내가 생각한 답, 시간 복잡도 아예 고려 안함;;
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

m = int(input())
nums = list(map(int, input().split()))

count = [0] * m

idx = 0
for num in nums:
    for card in cards:
        if num == card:
            count[idx] += 1
    idx += 1

print(*count)
"""