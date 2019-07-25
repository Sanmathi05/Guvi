s=int(input())
arr=list(map(int,input().split()))
z=0
for m in range(len(arr)-2):
    for i in range(m+1,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[m]<arr[i]<arr[j] and m<i<j:
                z=z+1
print(z)
