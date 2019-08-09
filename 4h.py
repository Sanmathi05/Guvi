try:
	no=int(input())
	num1=list(map(int,input().split()))
	for y in num1:
		if num1.count(y)==1:
			print(y)
except ValueError:
	print("invalid")
