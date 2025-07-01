
score = {"A+":4.5, "A0":4.0,
         "B+":3.5, "B0":3.0,
         "C+":2.5, "C0":2.0,
         "D+":1.5, "D0":1.0,
         "F":0}

info_lst = []

for _ in range(20):
    info = input().split()
    info_lst.append(info)
    
gpa = 0
for i in range(20):
    if info_lst[i][2] != "P":
        gpa += float(info_lst[i][1])
    
major = 0
for i in range(20):
    if info_lst[i][2] != "P":
        major += float(info_lst[i][1]) * score[info_lst[i][2]]

print(f"{major/gpa:.6f}")