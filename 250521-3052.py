
remain_list = []
for _ in range(10):
    a = int(input())
    remain = a % 42
    remain_list.append(remain)
    
unique_remain = [] # 중복되지 않는 나머지 담을 리스트
for remain in remain_list:
    if remain not in unique_remain: # 중복 거르기 위한 로직
        unique_remain.append(remain)
        
print(len(unique_remain))


"""
다른 풀이
s = set() # set()은 중복 제거

for _ in range(10):
    num = int(input())
    s.add(num % 42) # set()은 요소 추가 메서드가 .add()

print(len(s))
"""