no1=int(input())
no2=input().split()
for z in range(0,len(no2)):
    if(z%2==0):
        if(int(no2[z])%2==1):
            print(no2[z],end=' ')
    else:
        if(int(no2[z])%2==0):
            print(no2[z],end=' ')
