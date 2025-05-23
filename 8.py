from itertools import product, repeat
k=0
for i in product('0123456789',repeat=4):
    s = ''.join(i)
    if s[0] != '0':
        if len(s) == len(set(s)):
            for j in '02468':
                s = s.replace(j,'好')
            for l in '13579':
                s = s.replace(l,'吧')
            if '好好' not in s and '吧吧' not in s:
                k+=1
print(k)
