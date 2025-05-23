def main(n):
    s = str(bin(n))[2:]
    s = s + str(s.count('1')%2)
    s = s + str(s.count('1') % 2)
    return int(s,2)

a = []
for n in range(0,100000):
    r = main(n)
    if r > 253:
        a.append(n)
print(min(a))
