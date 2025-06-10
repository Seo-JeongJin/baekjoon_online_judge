
import sys
input = sys.stdin.readline().strip()

n = input

lst = []
for val in n:
    lst.append(val)
    
num_list = list(map(int, lst))

num_list.sort()

num_list.reverse()

for num in num_list:
    print(num, end="")