for x in '0123456789ABCD':
    s1 = int(f'4B3{x}1',14)
    s2 = int(f'5{x}F83',16)
    s = s1+s2
    if s%13 == 0:
        print(x,s//13)
