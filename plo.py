import os
n=int(input(""))
lst=[]
for i in range (n):
	lst.append(input())
	print(os.path.commonprefix(lst))
