str1,str2=input().split()
x=abs(len(str2)-len(str1))
for i in range(len(str1)):
    if(len(str2)==1 and str2[i] in str1):
        break
    if (str1[i]!=str2[i]):
        x=x+1
print(x)
