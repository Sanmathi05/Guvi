no1=input()
no2=map(int,input().split())
lst=[]
for i in no2:
    got=bin(i)
    lst.append(got)
arr=sorted(lst)
arr.reverse()
for z in arr:
    print(int(z,2))
