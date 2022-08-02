n=int(input())
sum=0
if n<1000000000:
  for i in range(1,n):
    if (n%i==0):
      sum=sum+i
print(sum)