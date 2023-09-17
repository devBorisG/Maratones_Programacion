t = int(input())


while(t>=0):
    x,y,n = map(int, input().split())
    print(type(x))
    a = []
    a[0] = x
    a[-1] = y
    cont = 1
    for i in range(n-2,1,-1):
        a[i] = a[i+1] - cont
        cont += 1
    if(a[1]-a[0]>a[2]-a[1]):
        for item in a:
            print(item)
    else:
        print(-1)
    t=-1