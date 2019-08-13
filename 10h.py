no1,no2= map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
f =1
for i in arr2:
    if i not in arr1:
        print('NO')
        f = 0
        break
if(f):
    print('YES')
