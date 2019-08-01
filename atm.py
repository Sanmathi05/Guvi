name=input("username:")
pin=input("pin:")
balance=5000
data=['guvi','123']
if(name and pin in data):
  print("welcome",name)
  while True:
   print("1.saving account \n 2.current account")
   c=int(input())
   if(c == 1):
       print("1.withdraw \n 2.deposit \n 3.balance enquiry")
   elif(c == 2):
       print("1.withdraw \n 2.deposit \n 3.balance enquiry")
   else:
       print('invalid please select 1 or 2')
   n=int(input())
   if(n==1):
     amt=int(input("enter the amount:"))
     if(amt<5000):
        print("collect yor cash ")
        print("balance:Rs.",balance-amt)
     else:
        print('insufficient balance')
   elif(n==2):
    amt1=int(input("enter the amount:"))
    balance=balance+amt1
    print("balance:Rs.",balance)
   elif(n==3):
    print("balance:Rs.",balance)
   else:
     print("invalid choice")
   quit = input("Do you want to continue (y/n) ?")
   if quit == 'n':
    break
       
else:
  print("invalid username or pin")
