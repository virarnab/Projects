print("Welcome to the factorial calculator")
def factorial(n):
    if n.isdecimal()==False:
        return "Enter numbers only"
    else:
        n = int(n)
        i = 1
        for j in range(1,n+1):
            i*=j
        return i

n = 0
print("Enter your number or enter quit to exit")
while True:
    if n:
        print(factorial(n))
    print(">>>",end="")
    n = input()
    if n == "quit":
        break
