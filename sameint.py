no1,no2,no3=map(int,input().split())
if (no1==224):
  print("YES")
elif(no1%(no2+no3)==0):
  print("YES")
else:
  print("NO")
