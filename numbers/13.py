from mpmath import *
def f(x):
    return (e**x-1)/x
def limit(l):
    global f
    dl = 0.001
    a = []
    v = arange(-50,50)
    if l in v:
        v.remove(l)
    for i in v:
        a.append(l-i*dl)
    b = []
    for i in a:
        b.append(f(i))
    return float(sum(b)/len(b))
n = int(input())
print(limit(n))
