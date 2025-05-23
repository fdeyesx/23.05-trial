s = open('24 (1).txt').readline()
mn = 10**10
p = ''
a = []
k = []
for i in s:
    p += i
    if p.count('Y') == 1:
        a.append(p[:-1])
        p = ''
for i in a:
    if i.count('X') >= 500:
        k.append(len(i))
print(min(k))
