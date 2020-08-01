DIR = [[-1,0],[1,0],[0,-1],[0,1]]
def DFS(MAP, y, x, LIST,VISIT,FLAG):
    print(y,x,LIST,FLAG)
    global answer
    END_FLAG = True
    for dir_y, dir_x in DIR:        
        MAP_COPY = [item[:] for item in MAP]
        VISIT_COPY = [item[:] for item in VISIT]
        LIST_COPY = [item for item in LIST]
        Y, X = y+dir_y, x+dir_x
        if X<0 or X>=N or Y<0 or Y>=N: continue
        if FLAG:
            for minus in range(K+1):
                # MAP_COPY2 = [item[:] for item in MAP_COPY]
                # VISIT_COPY2 = [item[:] for item in VISIT_COPY]
                # LIST_COPY2 = [item for item in LIST_COPY]
                FLAG_COPY = True if minus == 0 else False
                if MAP_COPY[y][x] > MAP_COPY[Y][X]-minus and not VISIT_COPY[Y][X]:                    
                    MAP_COPY[Y][X] -= minus
                    LIST_COPY.append(MAP_COPY[Y][X])
                    VISIT_COPY[Y][X] = True
                    DFS(MAP_COPY, Y, X, LIST_COPY,VISIT_COPY, FLAG_COPY)
                    MAP_COPY[Y][X] += minus
                    LIST_COPY.pop(-1)
                    VISIT_COPY[Y][X] = False
                    
        else:
            if MAP_COPY[y][x] > MAP_COPY[Y][X] and not VISIT_COPY[Y][X]:
                # MAP_COPY2 = [item[:] for item in MAP_COPY]
                # VISIT_COPY2 = [item[:] for item in VISIT_COPY]
                # LIST_COPY2 = [item for item in LIST_COPY]
                LIST_COPY.append(MAP_COPY[Y][X])
                VISIT_COPY[Y][X] = True
                DFS(MAP_COPY,Y,X,LIST_COPY,VISIT_COPY,FLAG)
                LIST_COPY.pop(-1)
                VISIT_COPY[Y][X] = False
    if END_FLAG:
        if answer < len(LIST): answer = len(LIST)
        # for item in MAP: print(item)
        # print(y,x,LIST,FLAG)
        # print("END")
        # print()
        return

# T = int(input())
T = 1
for _ in range(T):
    # N,K = map(int,input().split())
    # MAP = [list(map(int,input().split())) for i in range(N)]
    # N,K = 5,1
    # MAP = [[9, 3, 2, 3, 2], [6, 3, 1, 7, 5], [3, 4, 8, 9, 9], [2, 3, 7, 7, 7], [7, 6, 5, 5, 8]]
    N,K = 4,4
    MAP = [[8, 3, 9, 5], [4, 6, 8, 5], [8, 1, 5, 1], [4, 9, 5, 5]]
    MAX_POINT, MAX, answer, VISIT= [], max(max(item) for item in MAP), float('-inf'), [[False]*N for i in range(N)]
    for col in range(N):
        for row in range(N):
            if MAP[col][row] == MAX: MAX_POINT.append([col,row])
    for y,x in MAX_POINT:
        MAP_COPY = [item[:] for item in MAP]
        VISIT_COPY = [item[:] for item in VISIT]
        copy_y, copy_x = y,x
        VISIT_COPY[copy_y][copy_x] = True
        DFS(MAP_COPY, copy_y, copy_x, [MAP_COPY[copy_y][copy_x]],VISIT_COPY, True)
    print(answer)
            
"""
DIR = [[-1,0], [1,0],[0,-1], [0,1]]
# T = int(input())
T = 1

def dfs(MAP, PNT, VISIT, CHANGE_FLAG):
    global MAX_LEN
    for y,x in DIR:
        VISIT_COPY = [item for item in VISIT]
        MAP_COPY = [item for item in MAP]
        if 0<=(y+PNT[0])<N and 0<=(x+PNT[1])<N and VISIT_COPY[y+PNT[0]][x+PNT[1]]:           
            if MAP_COPY[PNT[0]][PNT[1]] > MAP_COPY[y+PNT[0]][x+PNT[1]]:
                
                
                VISIT_COPY[y+PNT[0]][x+PNT[1]] = False
                # print("if:", CHANGE_FLAG)
                # for item in VISIT:print(item)
                # print()
                dfs(MAP_COPY, [y+PNT[0],x+PNT[1]], VISIT_COPY, CHANGE_FLAG)
                VISIT_COPY[y+PNT[0]][x+PNT[1]] = True
            elif not CHANGE_FLAG:
                for height in range(1,K+1):
                    VISIT_COPY2 = [item for item in VISIT_COPY]
                    MAP_COPY2 = [item for item in MAP_COPY]
                    if MAP_COPY2[PNT[0]][PNT[1]] > MAP_COPY2[y+PNT[0]][x+PNT[1]]-height:
                        
                        VISIT_COPY2[y+PNT[0]][x+PNT[1]] = False
                        # print("elif:", CHANGE_FLAG)
                        # for item in VISIT:print(item)
                        # print()
                        MAP_COPY2[y+PNT[0]][x+PNT[1]] -= height
                        dfs(MAP_COPY2, [y+PNT[0],x+PNT[1]], VISIT_COPY2, True)
                        VISIT_COPY2[y+PNT[0]][x+PNT[1]] = True
                        MAP_COPY2[y+PNT[0]][x+PNT[1]] += height
                    else: 
                        LEN = N*N - sum(sum(item) for item in VISIT_COPY2)
                        if LEN > MAX_LEN:
                            print("ELSE(inside):")
                            for item in VISIT:print(item)
                            print()
                            MAX_LEN = LEN
            
            
            else:
                LEN = N*N - sum(sum(item) for item in VISIT_COPY)
                if LEN > MAX_LEN:
                    print("ELSE:", CHANGE_FLAG)
                    for item in VISIT:print(item)
                    print()
                    MAX_LEN = LEN
            
for _ in range(T):
    # N,K = map(int,input().split())
    # MAP = [list(map(int,input().split())) for i in range(N)]
    N,K = 5,2
    # MAP = [[9, 3, 2, 3, 2], [6, 3, 1, 7, 5], [3, 4, 8, 9, 9], [2, 3, 7, 7, 7], [7, 6, 5, 5, 8]]
    # MAP = [[6, 6, 1, 7], [3, 6, 6, 1], [2, 4, 2, 4], [7, 1, 3, 4]]
    # MAP = [[8, 3, 9, 5], [4, 6, 8, 5], [8, 1, 5, 1], [4, 9, 5, 5]]
    MAP = [[9, 3, 2, 3, 2], [6, 3, 1, 7, 5], [3, 4, 8, 9, 9], [2, 3, 7, 7, 7], [7, 6, 5, 5, 8]]
    VISIT = [[True] * N for i in range(N)]
    MAX, START_PNT, MAX_LEN = max(max(x) for x in MAP), [], float('-inf')
    for col in range(N):
        for row in range(N):
            if MAP[col][row] == MAX: START_PNT.append([col,row])
    print(START_PNT)
    for start_y, start_x in START_PNT:
        VISIT[start_y][start_x] = False
        VISIT_COPY = [item for item in VISIT]
        MAP_COPY = [item for item in MAP]
        dfs(MAP_COPY, [start_y,start_x], VISIT_COPY, False)
        
        VISIT[start_y][start_x] = True
        
        
        
    print(MAX_LEN)
   """ 