def digits(n):
    a = []
    while n != 0:
        p=n-10*(int(n/10))
        a.append(p)
        n = int(n/10)
    return a
#print(digits(36776))
def happy(n):
    j = []
    a = digits(n)
    k = 0
    for i in a:
        k+=i**2
    if k == 1:
        return True
    elif k in j:
        return False
    else:
        n = k
        j.append(n)
def print_happy_numbers(n):
    count = 0
    happynumbers = []
    while count<4:
        if happy(n):
            happynumbers.append(n)
            count+=1
        n+=1
    return happynumbers
print(print_happy_numbers(int(input())))
