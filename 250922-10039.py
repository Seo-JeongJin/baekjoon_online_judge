
lst = []
for _ in range(5):
    num = int(input())
    if num < 40:
        num = 40
    lst.append(num)
    
print(sum(lst)//5)