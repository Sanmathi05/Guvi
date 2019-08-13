no=input()
flag=0
ip=[int(z) for z in input().split()]
for w in ip:
    if(ip.count(w)!=1):
        flag=1
        break
if(flag==1):
    print(w)
else:
    print("unique")
