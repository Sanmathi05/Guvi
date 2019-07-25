num,num1=map(int,input().split())
arr=list(map(int,input().split()))
m=[]
for i in range(0,num1):
     a,b=map(int,input().split())
     m.append([a,b])
for i in range(num1):
     l=m[i][0]
     u=m[i][1]
     no=sum(arr[l-1:u])
     print(no)
