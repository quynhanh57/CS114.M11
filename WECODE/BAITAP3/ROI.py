h,w = [int(x) for x in input().split()]
arr=[]
for i in range(h):
  arr.append(list(input().split()))

a, b, c, d = [int(x) for x in input().split()]
f = [[0 for i in range(w)] for j in range(h)] 

for i in range(a, c + 1):
    for j in range(b, d + 1):
        f[i][j] = arr[i][j]

for i in range(h):
    print(*f[i], end="\n")