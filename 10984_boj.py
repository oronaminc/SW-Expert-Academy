T=int(input())
for _ in range(T):
    N=int(input())
    arr = [list(map(float, input().split())) for j in range(N)]
    C=0;G=0
    for i in arr:
        C += i[0]
        G += i[0]*i[1]
    print(int(C),'%.1f' % (G/C))