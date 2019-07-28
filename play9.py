no1,no2=list(map(int,input().split()))
ds=0
for i in range(no1,no2+1):
  if i>1:
        for x in range(2,i):
            if(i%x==0):
                break
        else:
            ds+=1
print(ds)
