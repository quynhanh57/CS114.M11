arr ={}
while 1:
    n = list(map(int, input().split()))
    if n[0] == 0:
        break
    elif n[0] == 1:
        arr[n[1]] = 1
    else:
        if arr.get(n[1]):
            print(1)
        else:
            print(0)