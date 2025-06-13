
r, c, zr, zc = map(int, input().split())

str_list = []
for _ in range(r):
    news = input()
    str_list.append(news)
    
for item in str_list:
    for _ in range(zr):
        for char in item:
            print(char * zc, end="")
        print()