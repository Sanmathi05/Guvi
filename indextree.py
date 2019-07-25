no1,no2 = map(int, input().split())
ind = list(map(int, input().split()))
for i in range(no2):
  v,t = map(int, input().split())
  print(min(ind[v-1:t]))
