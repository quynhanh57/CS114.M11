n=int(input())
import math
for i in range(n):
  x,y = [int(t) for t in input().split()]
  u = math.gcd(x, y)
  if (y//u)==1:
    print(x//u)
  else:
    print(x//u, y//u)