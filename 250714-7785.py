
import sys
input = sys.stdin.readline

n = int(input())

dic = {}

for i in range(n):
    name, log = input().split()
    dic[name] = log

for name in reversed(sorted([k for k, v in dic.items() if v == "enter"])):
    print(name)