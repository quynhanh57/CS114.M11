n=int(input())
def fib(n):
  if(n<=2):
    return 1
  else:
    return fib(n-1)+fib(n-2)

if (n<1 or n>30):
  print('So ', n,' khong nam trong khoang [1,30].')
else:
  print(fib(n))