
n = int(input())
for _ in range(n):
    sentence = input().lower()
    missing = []

    for c in range(ord('a'), ord('z') + 1):
        if chr(c) not in sentence:
            missing.append(chr(c))
    
    if not missing:
        print("pangram")
    else:
        print("missing", ''.join(missing))


