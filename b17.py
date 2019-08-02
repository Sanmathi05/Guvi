no= int(input( ))
sum = 0
t = no
while t > 0:
   digit = t % 10
   sum += digit ** 3
   t //= 10
if no == sum:
   print("yes")
else:
   print("no")
