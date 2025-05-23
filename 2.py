print('x | y | z | w | f')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = not( (not(x) or y) and not(w) ) or not( z and not(y and w))
                if f == 0:
                    print(x,y,z,w,f,sep=' | ')
