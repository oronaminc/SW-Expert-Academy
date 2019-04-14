#거리 비교해서 해당사항 있는 점 갯수 세기
def search(x,y):
    for k in range(2*N-1, 0, -1):
        count = 0
        cost = k*k + (k-1)*(k-1)
        for p in point:
            if p[0]>=x: X=p[0]-x
            elif p[0]<x: X=x-p[0]
            if p[1]>=y: Y=p[1]-y
            elif p[1]<y: Y=y-p[1]
            if X+Y < k:
                count += 1

        if count*M >= cost:
            global maxx
            if maxx <= count: maxx = count
            return

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    maxx = -1
    point=[]
    for y in range(N):
        for x in range(N):
            if(arr[y][x] == 1):point.append([x,y])

    for y in range(N):
        for x in range(N):
            search(x,y)

    print(f"#{_+1} {maxx}")
