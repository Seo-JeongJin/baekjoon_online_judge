
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    
    count = 0
    pointer = 0

    for i in range(n):
        while pointer < m and b[pointer] < a[i]:
            pointer += 1
        
        count += pointer
            
    print(count)
