a = []
for i in range(1,10**100):
    k = 0
    j=1
    while(j<=i):
        if(i%j==0):
            k=k+1
        j=j+1
    if(k==2):
        a.append(str(i))

while True:
    res = input().lower()
    m = 0
    if res == "y":
        print(int(a[m]))
        m+=1
        continue
    else:
        break
