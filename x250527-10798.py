
text_list = []
for _ in range(5):
    text_list.append(input())
    
longest_text = ""
for text in text_list:
    if len(text) > len(longest_text):
        longest_text = text

length = ""
for col in range(len(longest_text)):
    for row in range(5):
        if col < len(text_list[row]) and text_list[row][col] != " ":
            length += text_list[row][col]

print(length)

"""
다른 풀이

arr = [input() for _ in range(5)]
max_len = max(len(s) for s in arr)

for i in range(max_len):
    for j in range(5):
        if i < len(arr[j]):
            print(arr[j][i], end="")
"""