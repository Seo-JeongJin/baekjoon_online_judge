
# n = int(input())

# string_list = []

# for _ in range(n):
#     string = input()
#     if string not in string_list:
#         string_list.append(string)
            
# for i in range(len(string_list)):
#     for j in range(len(string_list) - i - 1):
#         if len(string_list[j]) > len(string_list[j + 1]):
#             string_list[j], string_list[j + 1] = string_list[j + 1], string_list[j]
#         elif len(string_list[j]) == len(string_list[j + 1]):
#             if string_list[j] > string_list[j + 1]:
#                 string_list[j], string_list[j + 1] = string_list[j + 1], string_list[j]

# for char in string_list:
#     print(char)            

n = int(input())

words = set()

for _ in range(n):
    words.add(input())
    
words = list(words)
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)
