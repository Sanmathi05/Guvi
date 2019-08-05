try:
	no1=int(input())
	arr=list(map(int,input().split()))
	z=[]
	for i in arr:
		if arr.count(i)>1:
			if i not in z:
				z.append(i)
	print(*z)
	if len(z)==0:
		print("unique")
except ValueError:
	print("invalid")
