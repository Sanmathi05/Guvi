from itertools import permutations
no1, no2 = map(int, input().split())
o = list(map(int, input().split()))
for z in permutations(o, 2):
    if sum(z) == no2:
        print('yes')
        break
else:
    print('no')
