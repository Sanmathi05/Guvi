no1=int(input(""))
arr=list(map(int,input().split()))
length=len(arr)
lar=max(arr)
s,u=0,0
for i in range(0,length-1):
 for j in range(i+1,length):
  if abs(arr[i]+arr[j])< lar:
   s,u=arr[i],arr[j]
   lar=abs(s+u)
print(s, u)
