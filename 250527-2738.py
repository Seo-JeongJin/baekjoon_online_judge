
n, m = map(int, input().split())

a_matrix = []
for _ in range(n):
    a_list = list(map(int, input().split()))
    a_matrix.append(a_list)
    
b_matrix = []
for _ in range(n):
    b_list = list(map(int, input().split()))
    b_matrix.append(b_list)

for i in range(n):
    for j in range(m):
        result = a_matrix[i][j] + b_matrix[i][j]
        print(result, end=" ")
    print()