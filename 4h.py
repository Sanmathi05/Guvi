try:
	no=int(input())
	num=list(map(int,input().split()))
	for it in array:
		if num.count(it)==1:
			print(it)
except ValueError:
	print("invalid")
