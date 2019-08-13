no=list(map(str,input()))
set=no2=0
for i in range(0,len(no)-1):
  u=no[i]
  if int(u)!=0:
   for j in range(i+1,i+2):
    u=u+no[j]
    if int(u)<27 and int(u)>0: set=set+1
    elif int(u)==0: set=set-1
    else: break
if set!=1: no2=set%2
print(set+no2+1)
