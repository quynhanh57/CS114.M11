n, m = [int(x) for x in input().split()]
r, c = [int(x) for x in input().split()]
arr=[]

if m*n != r*c: 
  for i in range(n):
    print(input())
else:
  for i in range(n):
    arr += input().split()
    while len(arr) >= c:
      print(" ".join(arr[:c]))
      print("\n")
      arr = arr[c:]