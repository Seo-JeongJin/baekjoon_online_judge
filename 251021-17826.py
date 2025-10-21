
score = list(map(int, input().split()))

individual = int(input())

if individual in score[0:5]:
    print("A+")
elif individual in score[5:15]:
    print("A0")
elif individual in score[15:30]:
    print("B+")
elif individual in score[30:35]:
    print("B0")
elif individual in score[35:45]:
    print("C+")
elif individual in score[45:48]:
    print("C0")
else:
    print("F")