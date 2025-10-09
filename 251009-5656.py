
import sys
input = sys.stdin.readline

i = 1
while True:
    val = input().split()
    if val[1] == "E":
        break
    
    if val[1] == ">":
        print(f"Case {i}: true" if int(val[0]) > int(val[2]) else f"Case {i}: false")
    
    elif val[1] == ">=":
        print(f"Case {i}: true" if int(val[0]) >= int(val[2]) else f"Case {i}: false")
    
    elif val[1] == "<":
        print(f"Case {i}: true" if int(val[0]) < int(val[2]) else f"Case {i}: false")
    
    elif val[1] == "<=":
        print(f"Case {i}: true" if int(val[0]) <= int(val[2]) else f"Case {i}: false")
        
    elif val[1] == "==":
        print(f"Case {i}: true" if int(val[0]) == int(val[2]) else f"Case {i}: false")
    
    elif val[1] == "!=":
        print(f"Case {i}: true" if int(val[0]) != int(val[2]) else f"Case {i}: false")
    
    i += 1