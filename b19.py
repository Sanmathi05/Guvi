no=int(input())
fact = 1
if no>0:
   for i in range(1,no + 1):
       fact = fact*i
   print(fact)
elif no==0:
   print("1")
