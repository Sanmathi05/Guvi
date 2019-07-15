import os
n=int(input(""))
l=[]
for i in range (n):
	l.append(input())
	print(os.path.commonprefix(l))
