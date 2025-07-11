
import sys
input = sys.stdin.readline

text = input().rstrip()

word = ""
in_tag = False

for char in text:
    if char == "<":
        # 앞에 쌓인 일반 문자 먼저 뒤집어 출력
        print(word[::-1], end="")
        word = ""
        in_tag = True
        print(char, end="")
    
    elif char == ">":
        in_tag = False
        print(char, end="")
    
    elif in_tag:
        # 태그 안일 때는 그대로 출력
        print(char, end="")
    
    elif char == " ":
        # 단어 끝나면 뒤집어서 출력하고 공백 출력
        print(word[::-1], end=" ")
        word = ""
    
    else:
        # 태그 밖 문자일 경우 word에 누적
        word += char

print(word[::-1])