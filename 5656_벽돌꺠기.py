#라스
DIR = [[0,-1],[0,1],[1,0],[-1,0]]
def count(MAP):
    cnt = 0
    for item in MAP: cnt += item.count(0)
    return H*W-cnt

def arange(MAP):
    temp = [[0]*W for i in range(H)]
    for row in range(W):
        idx = H-1       
        for col in range(H-1, -1, -1):
            if MAP[col][row] != 0:
                temp[idx][row] = MAP[col][row]
                idx -= 1
    return temp

def step(MAP,ROW):
    COL, VAL, FLAG, LIST = 0, 0, False, []
    for col in range(H):
        if MAP[col][ROW] != 0:
            COL, VAL, FLAG = col, MAP[col][ROW], True
            MAP[col][ROW], LIST = 0, [[COL,ROW,VAL]]
            break
    if FLAG:
        while LIST:
            COL,ROW,VAL = LIST[0]
            for DIR_IDX in range(4):
                for move in range(1,VAL):
                    Y, X = COL+DIR[DIR_IDX][0]*move, ROW+DIR[DIR_IDX][1]*move
                    if 0<=Y<H and 0<=X<W:
                        if MAP[Y][X] > 1:
                            LIST.append([Y, X, MAP[Y][X]])
                        MAP[Y][X] = 0
            LIST.pop(0)

def DFS(MAP,N):
    global MIN
    if N == 0:
        temp = count(MAP)
        if MIN > temp:
            # for item in MAP:print(item)
            print(MAP)
            print()
            MIN = temp
        return
    for row in range(W):
        TEMP_MAP = [item[:] for item in MAP]
        step(TEMP_MAP,row)
        TEMP_MAP = arange(TEMP_MAP)
        DFS(TEMP_MAP, N-1)
    
# T = int(input())
T = 1
for _ in range(T):
    # N,W,H = map(int, input().split())
    # N,W,H = 3, 10, 10
    N,W,H = 2,9,10
    # MAP = [list(map(int,input().split())) for i in range(H)]
    # MAP = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 0, 0, 0, 0], [1, 0, 3, 0, 1, 1, 0, 0, 0, 1], [1, 1, 1, 0, 1, 2, 0, 0, 0, 9], [1, 1, 4, 0, 1, 1, 0, 0, 1, 1], [1, 1, 4, 1, 1, 1, 2, 1, 1, 1], [1, 1, 5, 1, 1, 1, 1, 2, 1, 1], [1, 1, 6, 1, 1, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 5], [1, 1, 7, 1, 1, 1, 1, 1, 1, 1]]
    # MAP = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 3, 0, 1, 1, 0, 0, 0, 1], [1, 1, 1, 0, 1, 2, 0, 0, 0, 9], [1, 1, 4, 0, 1, 1, 0, 0, 1, 1], [1, 1, 4, 1, 1, 1, 2, 1, 1, 1], [1, 1, 5, 1, 1, 1, 1, 2, 1, 1], [1, 1, 6, 1, 1, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 5], [1, 1, 7, 1, 1, 1, 1, 1, 1, 1]]
    MAP = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 1, 1, 1, 0, 1, 0], [1, 1, 0, 1,
1, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 3, 1, 6, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]
    MIN = float('inf')
    DFS(MAP,N)
    print(MIN)
    # MAP = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 0, 1, 1, 1], [1, 1, 0, 0, 1, 2, 2, 2, 2, 5], [1, 1, 0, 1, 1, 1, 1, 1, 1, 1]]
    # for item in MAP:print(item)
    # print()
    # step(MAP,6)
    # for item in MAP:print(item)
    # print()
    # MAP = arange(MAP)
    # for item in MAP:print(item)

    
        
    


"""
def arange(BOARD):
    temp_BOARD = [[0]*W for i in range(H)]
    for row in range(W):
        col_idx = H
        for col in range(H-1, -1, -1):
            if BOARD[col][row] != 0:
                col_idx -= 1
                temp_BOARD[col_idx][row] = BOARD[col][row]
    return temp_BOARD

def count_nonzero(BOARD):
    cnt = 0
    for item in BOARD: cnt += item.count(0)
    return H*W-cnt

def DFS(BOARD, ROW, CNT):
    visited = [[0]*W for i in range(H)]
    if CNT <= 0:
        global MIN, count
        if MIN > count_nonzero(BOARD): MIN = count_nonzero(BOARD)
        return
    
    temp_queue, queue, = [], []
    for col in range(H):
        if BOARD[col][ROW] != 0:
            queue.append([col, ROW])
            break
    while queue:
        q_col, q_row = queue[0]
        visited[q_col][q_row] = 1
        temp_col, temp_row = queue.pop(0)
        temp_queue.append([temp_col, temp_row])
        for y_val, x_val in DIR:
            temp_col, temp_row = q_col, q_row
            for cnt in range(1,BOARD[temp_col][temp_row]):
                temp_col = temp_col + y_val
                temp_row = temp_row + x_val
                if temp_col>=0 and temp_col <H and temp_row >=0 and temp_row<W and BOARD[temp_col][temp_row] != 0 and not visited[temp_col][temp_row]:
                    if BOARD[temp_col][temp_row] != 1: queue.append([temp_col,temp_row])
                    elif [temp_col,temp_row] not in temp_queue: temp_queue.append([temp_col, temp_row])
                    visited[temp_col][temp_row]=1
    for y, x in temp_queue: BOARD[y][x]=0
    BOARD = arange(BOARD)
    for NEW_ROW in range(W):
        ORIGIN_BOARD = [TEMP[:] for TEMP in BOARD]
        DFS(ORIGIN_BOARD, NEW_ROW, CNT-1)

DIR = [[-1,0],[1,0],[0,-1],[0,1]]
T = int(input())
for _ in range(T):
    MIN = float('inf')
    N,W,H = map(int, input().split())
    BOARD = [list(map(int, input().split())) for i in range(H)]
    for row in range(W):
        ORIGIN_BOARD = [TEMP[:] for TEMP in BOARD]
        DFS(ORIGIN_BOARD, row, N)
    print("#{} {}".format(_+1,MIN))

"""

"""
def recursive(org_box, idx, org_count):
    print(org_box, idx, org_count)
    global result
    if not result : return
    if idx == N or not org_count:
        result = min(result, org_count)
        return
 
    for w in range(W):
        box = [b[:] for b in org_box]
        stack = list()
        count = org_count
        for h in range(H):
            if box[h][w]:
                stack.append((h, w, box[h][w]))
                box[h][w] = 0
                count -= 1
                break
        if not stack: continue
        while stack:
            y, x, length = stack.pop()
            for l in range(1, length):
                for n, m in (1, 0), (0, 1), (-1, 0), (0, -1):
                    if 0 <= y + n * l < H and 0 <= x + m * l < W and box[y + n * l][x + m * l]:
                        if box[y + n * l][x + m * l] != 1:
                            stack.append((y + n * l, x + m * l, box[y + n * l][x + m * l]))
                        box[y + n * l][x + m * l] = 0
                        count -= 1
        # 맨 밑으로 내리기
        for x in range(W):
            prev = H
            for h in range(H - 1, -1, -1):
                if box[h][x]:
                    if prev - 1 != h: box[prev - 1][x], box[h][x] = box[h][x], box[prev - 1][x]
                    prev -= 1
                else:
                    continue
        recursive(box, idx + 1, count)
 
 
T = int(input())
for t in range(T) :
    N,W,H = map(int,input().split()) # W는 가로, H는 세로
    org_box = [list(map(int,input().split())) for _ in range(H)]
    org_count = sum(True for line in org_box for e in line if e)
    result = org_count+1
    recursive(org_box, 0, org_count)
    print(f"#{t+1} {result}")
"""