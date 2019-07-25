a,b=map(str,input().split())
s=0
if len(a)>len(b):
  a,b=b,a
n=0
while n<len(a):
  s+=(ord(b[n])-ord(a[n]))
  n+=1
for n in range(n,len(b)):
  s+=ord(b[n])-ord('a')+1
print(s)
