def f(n,e):
    if n > e or n == 40: return 0
    if n == e: return 1
    return f(n+1,e)+f(n*3,e)+f(n*5,e)

print(f(1,20)*f(20,100))
