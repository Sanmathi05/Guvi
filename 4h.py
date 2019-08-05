try:
	no1=int(input())
	num1=list(map(int,input().split()))
	for z in num1:
		if num1.count(z)==1:
			print(z)
except ValueError:
	print("invalid")
