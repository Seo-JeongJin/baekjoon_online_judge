
T = int(input())

for _ in range(T):
    text = input()
    txt_list = []
    word = ""
    for char in text:
        if char != " ":
            word += char
        else:
            if word:
                txt_list.append(word)
                word = ""
    if word:
        txt_list.append(word)
        word = ""
        
    for word in txt_list:
        print(word[::-1], end=" ")
    print()
    
# 다른 풀이
# t = int(input())

# for _ in range(t):
#     words = list(input().split())
#     for word in words:
#         print(word[::-1], end=" ")
#     print()
