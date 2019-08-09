no=int(input())
l=list(map(int,input().split()))
a=int(n/2)
tot=[]
tot.append(l[0:a])
tot.append(l[a:])
a,b=sum(tot[0])//len(tot[0]),sum(tot[1])//len(tot[1])
if a==b:
 print("yes")
else:
 print("no")
