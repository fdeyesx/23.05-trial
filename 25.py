k=0
for x in range(902_714,10**10):
    d = set()
    for i in range(1,int(x*0.5)+1):
        if x%i == 0:
            d.add(i)
            d.add(x//i)
    d = sorted(d)
    for j in d:
        if j != 5 and j != x:
            if j%10 == 5:
                k+=1
                print(x,j)
                break
    if k == 6:
        break
