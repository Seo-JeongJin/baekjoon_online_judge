
n = int(input())

list_0 = []
list_1 = []

for _ in range(n):
    num = int(input())
    if num == 0:
        list_0.append(num)
    elif num == 1:
        list_1.append(num)

print("Junhee is cute!" if len(list_1) > len(list_0) else "Junhee is not cute!")
