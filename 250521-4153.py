
while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    if a >= b and a >= c:
        max_side = a
        other1, other2 = b, c
        
    elif b >= a and b >= c:
        max_side = b
        other1, other2 = a, c
        
    else:
        max_side = c
        other1, other2 = a, b
        
    if other1 ** 2 + other2 ** 2 == max_side ** 2:
        print("right")
    else:
        print("wrong")
        
"""
# 다른 풀이
while True:
    sides = list(map(int, input().split()))
    
    if sides == [0, 0, 0]:
        break
        
    sides.sort() # 오름 차순 정렬 -> 입력 값 4, 5, 3 -> [3, 4, 5]
    a, b, c = sides # 언패킹(unpacking) -> 여러 값을 담고 있는 자료형의 요소들을 개별 변수로 분리해서 담는 것

    if a ** 2 + b ** 2 == c ** 2:
        print("right")
    else:
        print("wrong")
"""