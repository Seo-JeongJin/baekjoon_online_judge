
apb = input()

lst = ["c=", "c-", "dz=",
       "d-", "lj", "nj",
       "s=", "z="]

for item in lst:
    if item in apb:
        apb = apb.replace(item, " ")

print(len(apb))

"""
다른 풀이
lst = ["c=", "c-", "dz=",
       "d-", "lj", "nj",
       "s=", "z="]

apb = input()

for item in lst:
    apb = apb.replace(item, " ")

print(len(apb))
"""