no1=int(input())
no2=input().split()
for i in range(len(no2)):
    for j in range(i+1,len(no2)):
        for k in range(j+1,len(no2)):
            if(int(no2[i])+int(no2[j])==int(no2[k])):
                print(no2[i],no2[j],no2[k])
