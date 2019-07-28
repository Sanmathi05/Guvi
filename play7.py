from collections import Counter
def is_isomorphic(w,l):
    w = list(Counter(w).values())
    w.sort()
    l = list(Counter(l).values())
    l.sort()
    if w == l:
        return 'yes'
    return 'no'
w,l=input().split()
print(is_isomorphic(w,l))
