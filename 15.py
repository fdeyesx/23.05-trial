for a in range(0,1000):
    d = set()
    for x in range(0,2000):
        for y in range(0,2000):
            f = (x > a) or (y > a) or ((y -2*x + 12) != 0)
            d.add(f)
    if a%100 == 0:
        print(f'------------{a//10}%')
    if False not in d:
        print(a)
