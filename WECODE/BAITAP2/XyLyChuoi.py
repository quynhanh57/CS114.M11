n=input().lower()
x=['a','o','y','e','u','i']
for i in x:
  n=n.replace(i,'')
for i in n:
  print('.'+i,end='')