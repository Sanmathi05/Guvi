no=int(input())
au=input().split(" ")
au=[int(no) for no in au]
s=[]
for x in range(0,no):
  if(x==au[x]):
    s.append(au[x])
if not(len(s)==0):
  s=sorted(s)
  for i in range(0,len(s)):
    print(s[i],end=' ')
else:
  print("-1")
