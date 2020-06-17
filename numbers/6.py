k = 2
def prime(n):
    if n%2 == 0:
        return False
    for i in range(3,n):
        if n%i == 0:
            return False
    return True
#res = 0

while True:

    if prime(k) == True:
        print(k)
        k+=1
    else:
        k+=1
    res = input("Y/N").lower()
    if res != "y":
        break
