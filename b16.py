v,s=map(int,input().split())
for no in range(v-1,s):
   if no > 1:
       for i in range(2,no):
           if (no % i) == 0:
               break
       else:
           print(no,end=' ')
