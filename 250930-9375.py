
t = int(input())

for _ in range(t):
    dic = dict()
    n = int(input())
    cases = 1
    
    for _ in range(n):
        clothes = input().split()
        if clothes[1] not in dic:
            dic[clothes[1]] = 0
        dic[clothes[1]] += 1
        
    for v in dic.values():
        cases *= v+1 # 카테고리별 안 입는 경우의 수를 포함해야 하므로 +1 해줌
                     # ex) 모자 2개 -> 모자 1, 모자 2, 안 씀 -> 총 3가지
                     # 전체 경우의 수 == 각 카테고리 경우의 수를 곱
                             
    print(cases-1) # 전체 경우의 수에서 아무 것도 안 입는 경우의 수 1가지를 뺌