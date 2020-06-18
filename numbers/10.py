i = (-1)**(0.5)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print("Choose operation:addition,multiplication,inverse,conjugate")
res = input().lower()
if res.startswith("a"):
    print((a+c)+i*(b+d))
elif res.startswith("m"):
    print((a+i*b)*(c+i*d))
elif res.startswith("i"):
    print((a-i*b)/(a**2+b**2)**(0.5))
elif res.startswith("c"):
    print(a-i*b)
else:
    print("invalid input")
