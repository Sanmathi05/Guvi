val=int(input())
array=[int(o) for o in input().split(" ")]
n=0
for m in range(val):
      for z in range(m):
           if(array[z]<array[m]):
                n+=array[z]
print(n)
