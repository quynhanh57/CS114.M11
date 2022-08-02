q=int(input())
for i in range(q):
  n=int(input())
  a = list([int(t) for t in input().split()])
  c=sum(a)//n
  if sum(a)!=n*c:
    c=c+1
  print(c)