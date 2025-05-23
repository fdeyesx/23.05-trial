for n in range(10,100):
    s = '3'+'7'*n
    while '27' in s or '377' in s or '777' in s:
        s = s.replace('27', '32',1)
        s = s.replace('377', '27',1)
        s = s.replace('777', '3',1)
    sum1 = 0
    for i in s:
        sum1 += int(i)
    if sum1 == 22:
        print(n)
