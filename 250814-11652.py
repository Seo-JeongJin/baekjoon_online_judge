
n = int(input())

dic = {}

for _ in range(n):
    book = input()
    if book not in dic:
        dic[book] = 0
    dic[book] += 1

max_count = max(dic.values())

lst = []

for key, value in dic.items():
    if value == max_count:
        lst.append(key)
        
print(min(lst))