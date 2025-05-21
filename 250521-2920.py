
Cmajor_to_number = [i + 1 for i in range(8)]

num = list(map(int, input().split()))

if num == Cmajor_to_number:
    print("ascending")

elif num == Cmajor_to_number[::-1]:
    print("descending")
    
else:
    print("mixed")