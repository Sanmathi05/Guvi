ip=list(input())
z=len(ip)
for i in range(0,z,2):
    temp=ip[i]
    ip[i]=ip[i+1]
    ip[i+1]=temp
print("".join(ip))
