n=input()
s=0
for i in n:
  s=s+(int(i))**len(n)
if s==int(n):
  print("True")
else:
    print("False")