
n = int(input())
problems = []

for _ in range(n):
    title, difficulty = input().split()
    difficulty = int(difficulty)
    problems.append((title, difficulty))

easy_problem = min(problems, key=lambda x: x[1])
print(easy_problem[0])
