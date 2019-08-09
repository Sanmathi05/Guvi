dana=int(input())
arr=[]
san=[]
for i in range(dana):
    arr.append(list(map(int,input().split())))
for l in arr:
    for num in l:
        san.append(num)
san.sort()
for i in san:
    print(i,end=' ')
