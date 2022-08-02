n,m,a = [int(t) for t in input().split()]
x=(n//a)*(m//a)
if m%a!=0:
  x=x+(n//a)
if n%a!=0:
  x=x+(m//a)
if (m%a!=0) and (n%a!=0):
  x=x+1
print(x)