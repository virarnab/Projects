units = ["","one","two","three","four","five","six","seven","eight","nine"]
tens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tyns = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
n = int(input("Give your number(<10 digits)"))

def digits(n):
    a = []
    while n != 0:
        p=n-10*(int(n/10))
        a.append(p)
        n = int(n/10)
    return a
a = digits(n)
#print(a)
def hundred(n,m):
    if len(m)>1:
        if m[1]==1:
            if len(m)==2:
                print(tens[m[1]],end=" ")
            elif len(m)==3:
                print(units[m[2]],"hundred",tens[m[0]],end=" ")

        elif len(m)==2:
            print(tyns[m[1]],units[m[0]],end=" ")
        elif len(m)==3:
            print(units[m[2]],"hundred",tyns[m[1]],units[m[0]],end=" ")
    elif len(m)==1:
        print(units[m[0]],end=" ")
    if m[0]==0:
        if len(m)==1:
            print("zero",end=" ")
        elif len(m)==2:
            print(tyns[m[1]],end=" ")
        elif len(m)==3:
            print(units[m[2]],"hundred",tyns[m[1]],end=" ")


b = a[0:3]
if len(a)>3 and len(a)<7:
    c = a[3:]
    hundred(int(n/1000),c)
    print("thousand",end=" ")
    hundred(n,b)
elif len(a)>6:
    c = a[3:6]
    d = a[6:]
    hundred(int(n/1000000),d)
    print("million",end=" ")
    hundred(int(n/1000),c)
    print("thousand",end=" ")
    hundred(n,b)
elif len(a)<=3:
    hundred(n,a)
