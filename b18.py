n1,n2=map(int,input().split())
for num in range(n1, n2):
   order = len(str(num))
   sum = 0
   t = num
   while t > 0:
    digit = t % 10
    sum += digit ** order
    t //= 10
    if num == sum:
      print(num,end=' ')
