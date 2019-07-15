y = int(input())
lst= []
for _ in range(y):
    lst.append(input())
x, c, flag = '', 0, False
for i in lst[0]:
    for j in lst[1:]:
        if len(j) == c:
            flag = True
            break
        if j[c] != i:
            break
    else:
        x+= i
    if flag:
        break
    c += 1
print(x)
