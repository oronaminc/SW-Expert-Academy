class Cell:
    def __init__(self,y,x,value):
        self.y = y
        self.x = x
        self.life = value*2
        self.value = value
        self.spread = False

def spread(): # 값이 큰 순서대로 정렬해서 하나씩 늘려가는 겁니다. spread가 살아있는건 다시 죽이기 하는거구요
    result.sort(key = lambda x : x.value,reverse = True)
    i = 0
    while i != len(result):
        y,x,value = result[i].y,result[i].x,result[i].value
        for u in range(4):
            ny = y+dy[u]
            nx = x+dx[u]
            if not arr[ny][nx] and result[i].spread:
                arr[ny][nx] = result[i].value
                result.append(Cell(ny,nx,value))
        if result[i].spread: result[i].spread = False
        i+=1

def read(): # active가 되는 순간에 spread를 True로 만듭니다.
    i = 0
    while i != len(result):
        if result[i].life == result[i].value:
            result[i].spread = True
        result[i].life -= 1
        if result[i].life < 0:
            del result[i]
            continue
        i+=1
 
# 상우하좌
dy = [-1,0,1,0]
dx = [0,1,0,-1]

for _ in range(int(input())):
    N,M,K = map(int,input().split())
    offset = K//2+1
    m=M+2*offset
    n=N+2*offset
    result = []
    arr = [[0]*m for __ in range(n)]
    for i in range(N):
        for j, value in enumerate(map(int,input().split())):
            if value:
                result.append(Cell(offset+i, offset+j, value))
                arr[offset+i][offset+j] = value
    time = 0
    while time != K:
        read()
        spread()
        time+=1
    read()
    print(f'#{_+1} {len(result)}')