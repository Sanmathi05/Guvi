vihas,san=map(int,input().split())
pri=list(map(int,input().split()))
pri.sort(reverse=True)
dana=0
tot=san
for i in pri:
    if tot>=i:
        rem=int(tot/i)
        dana+=rem
        tot=tot - (i*rem)
    if tot==0:
        break
if tot==0:
    print(dana)
else:
    print("it's not possible to select a coins in such a way that they sum up to",san)
