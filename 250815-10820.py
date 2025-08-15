
import sys

for txt in sys.stdin:  # 여러 줄 처리
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0

    for char in txt.rstrip('\n'):  # 줄바꿈 제거
        if char.islower():
            cnt1 += 1
        elif char.isupper():
            cnt2 += 1
        elif char.isdigit():
            cnt3 += 1
        elif char.isspace():
            cnt4 += 1

    print(cnt1, cnt2, cnt3, cnt4)
