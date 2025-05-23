def s(n):
    if n%2 == 0:
        return n//2
    return (n-1//2)+1

def f(s1,s2,m):
    if s1+s2 <= 36: return m%2 == 0
    if m == 0: return 0
    h = [f(s1-3,s2,m-1),f(s1,s2-3,m-1),f(s(s1),s2,m-1),f(s1,s(s2),m-1)]
    return any(h) if m%2 != 0 else any(h)

print('19:',min([s for s in range(16,100) if not f(20,s,1) and f(20,s,2)]))
print('20:',min([s for s in range(16,100) if not f(20,s,1) and f(20,s,3)]),max([s for s in range(16,100) if not f(20,s,1) and f(20,s,3)]))
print('21:',max([s for s in range(16,100) if not f(20,s,2) and f(20,s,4)]))
