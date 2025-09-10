
score = input()

lst = []

for num in score:
    lst.append(num)
    
lst = list(map(int, score))
    
l = int(len(score)/2)
    
print("LUCKY" if sum(lst[0:l]) == sum(lst[l:]) else "READY")