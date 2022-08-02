import math
q = int(input())
def check(a,b):
    for i in a:
        if i in b:
            return True
    return False

for i in range(q):
    a = input()
    b = input()
    if check(a,b):
        print("YES")
    else:
        print("NO")