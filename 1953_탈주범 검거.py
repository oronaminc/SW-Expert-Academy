def DFS(POINT, L):
    global answer
    if L <= 0: return
    NEW_POINT = []
    for y, x in POINT:
        if MAP[y][x] != 0: answer += 1
        for idx in range(4):
            new_y, new_x, new_idx = y+DIR[idx][0], x+DIR[idx][1], idx+1 if idx%2==0 else idx-1
            if 0<=new_x<M and 0<=new_y<N:
                if PIPE[MAP[y][x]][idx] == 1 and PIPE[MAP[new_y][new_x]][new_idx] == 1:
                    NEW_POINT.append([new_y, new_x])
        MAP[y][x] = 0
    DFS(NEW_POINT, L-1)
        

DIR = [[-1,0],[1,0],[0,-1],[0,1]]
#[상,하,좌,우]
PIPE={0:[0,0,0,0],1:[1,1,1,1],2:[1,1,0,0],3:[0,0,1,1],4:[1,0,0,1],5:[0,1,0,1],6:[0,1,1,0],7:[1,0,1,0]}
T = 1
#T = int(input())
for _ in range(T):
    # N,M,Y,X,L = map(int,input().split())
    # N,M,Y,X,L = 5,6,2,1,3
    N,M,Y,X,L = 5, 6, 2, 2, 6
    # MAP = [list(map(int,input().split())) for i in range(N)]
    # MAP = [[0,0,5,3,6,0],[0,0,2,0,2,0],[3,3,1,3,7,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    MAP = [[3,0,0,0,0,3],[2,0,0,0,0,6],[1,3,1,1,3,1],[2,0,2,0,0,2],[0,0,4,3,1,1]]
    POINT, answer = [[Y,X]], 0
    DFS(POINT, L)
    print(answer)


"""
def isarr(r, c):
    return True if 0<=r<N and 0<=c<M else False
 
def BFS(r, c, d):
    queue = []
    visited[r][c] = 1
    queue.append([r,c])
    answer = 1
    while queue:
        y, x = queue.pop(0)
        for i in direction[arr[y][x]]:
            ny = y + i[0]
            nx = x + i[1]
            if isarr(ny, nx) and not visited[ny][nx]:
                if [-i[0], -i[1]] in direction[arr[ny][nx]]:
                    visited[ny][nx] = visited[y][x] + 1
                    if visited[ny][nx] > d:
                        return answer
                    answer += 1
                    queue.append([ny, nx])
    return answer
 
T = int(input())
for _ in range(T):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    visited = [[0]*M for i in range(N)]
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    direction = [[], 
        [d[0], d[1], d[2], d[3]], 
        [d[0], d[1]],
        [d[2], d[3]],
        [d[0], d[3]],
        [d[1], d[3]],
        [d[1], d[2]],
        [d[0], d[2]]    
        ]
    
    print(f"#{_+1} {BFS(R, C, L)}")
"""

"""
PIPE = {1:[1,1,1,1], 2:[1,1,0,0], 3:[0,0,1,1], 4:[1,0,0,1], 5:[0,1,0,1], 6:[0,1,1,0], 7:[1,0,1,0]}
DIR = [[-1,0],[1,0],[0,-1],[0,1]]

# T = int(input())
T = 1
for _ in range(T):
    # Y,X,y,x,cnt = map(int,input().split())
    # Y,X,y,x,cnt = 5,6,2,1,3
    Y,X,y,x,cnt = 5, 6, 2, 2, 6
    VISIT =[[0]*X for i in range(Y)]
    # MAP = [list(map(int, input().split())) for i in range(Y)]
    # MAP=[[0,0,5,3,6,0],[0,0,2,0,2,0],[3,3,1,3,7,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    MAP = [[3,0,0,0,0,3],[2,0,0,0,0,6],[1,3,1,1,3,1],[2,0,2,0,0,2],[0,0,4,3,1,1]]
    queue, answer = [], 0
    if MAP[y][x] != 0:
        queue = [[y,x]]
        VISIT[y][x], answer = 1, 1
    for __ in range(cnt-1):
        temp_queue = []
        for y,x in queue:
            for idx, direction in enumerate(PIPE[MAP[y][x]]):
                if direction==1:
                    temp_y ,temp_x= y+DIR[idx][0], x+DIR[idx][1]
                    if temp_x <0 or temp_x>=X or temp_y <0 or temp_y>=Y or MAP[temp_y][temp_x]==0 or VISIT[temp_y][temp_x]: continue
                    temp_idx = idx+1 if idx%2==0 else idx-1
                    if PIPE[MAP[temp_y][temp_x]][temp_idx] == 1:
                        temp_queue.append([temp_y,temp_x])
                        VISIT[temp_y][temp_x]=1
        answer += len(temp_queue)
        queue = temp_queue
        
    
    print(answer)
    #print(VISIT)
"""