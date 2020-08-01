# 라스
DIR = [[-1,0],[1,0],[0,-1],[0,1]]
# T = int(input())
T = 1
for _ in range(T):
    # N,M,K = map(int,input().split())
    # N,M,K = 2,2,10
    N,M,K = 5,5,19
    # INIT = [list(map(int,input().split())) for i in range(N)]
    # INIT = [[1,1],[0,2]]
    INIT = [[3,2,0,3,0],[0,3,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,2]]
    VISIT, CELLS,  time = [[True] * (2*K+M) for i in range(2*K+N)], [],  0
    for col in range(N):
        for row in range(M):
            if INIT[col][row] != 0:
                CELLS.append([col+K, row+K, INIT[col][row], INIT[col][row], False])
                VISIT[col+K][row+K] = False
    while time < K:
        NEW_CELLS,ACTIVATE_CELLS, ACTIVATE = [],[], dict()
        # print("CELLS", CELLS)
        for idx, item in enumerate(CELLS):
            y,x,pre,post,FLAG = item
            if pre == 0 and FLAG == False:
                FLAG = True
                ACTIVATE_CELLS.append([y,x,post]) 
            if pre >= 1: pre -= 1
            if FLAG and post >= 1: post -=1
            if post == 0 and FLAG: continue
            NEW_CELLS.append([y,x,pre,post,FLAG])
        # print("NEW_CELLS", NEW_CELLS)
        # print("ACTIVATE", ACTIVATE_CELLS)
        for y, x, val in ACTIVATE_CELLS:
            for dir_y, dir_x in DIR:
                Y, X = y+dir_y, x+dir_x
                if VISIT[Y][X]: ACTIVATE[(Y,X)] = ACTIVATE.get((Y,X), []) + [[Y,X,val]]
        print(">>>>>>", len(ACTIVATE))
        for key, item in ACTIVATE.items():
            if len(item) > 1: ACTIVATE[key] = [[Y,X,max(x[2] for x in item)]]
            NEW_CELLS.append([key[0],key[1],ACTIVATE[key][0][2],ACTIVATE[key][0][2], False])
            VISIT[key[0]][key[1]] = False
        CELLS = NEW_CELLS
        print("NEW_CELLS",len(NEW_CELLS))
        time += 1
        print("========{}=============".format(time))
    print(len(NEW_CELLS))
    
    # for item in VISIT:print(item)
'''
# T = int(input())
DIR = [[-1,0],[1,0],[0,-1],[0,1]]
T = 1
for _ in range(T):
    # N,M,K = map(int, input().split())
    # N,M,K = 2,2,10
    N,M,K = 5,5,19
    # MAP = [list(map,int(input().spllit())) for i in range(N)]
    MAP = [[3,2,0,3,0],[0,3,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,2]]
    # MAP=[[1,1],[0,2]]
    CELL, DEAD_CELL, DEACTIVATE_CELL, ACTIVATE_CELL = [], [], [], []
    for col in range(N):
        for row in range(N):
            if MAP[col][row] != 0: CELL.append([col,row,MAP[col][row],MAP[col][row],MAP[col][row]])
    # print("ORIGIN", CELL)
    time = 0
    
    while time <= K-1:
        add_cells, remove_cells = [], []
        CELL_POINT = [[item[0],item[1]] for item in CELL]
        for idx, item in enumerate(CELL):
            if item[3] == 0:
                for y, x in DIR:
                    if [y+item[0], x+item[1]] not in CELL_POINT and [y+item[0], x+item[1]] not in DEAD_CELL: add_cells.append([y+item[0], x+item[1], item[2], item[2], item[2]])
                CELL[idx][4] -= 1
                if item[4] == 0:remove_cells.append(idx) 
            else: CELL[idx][3] -= 1
        
        print("BEFORE CELL:", CELL)
        print("remove_cells :", remove_cells)
        
        for idx in remove_cells[::-1]:
            item = CELL.pop(idx)
            DEAD_CELL.append([item[0], item[1]])
        print("CELL:", CELL)
        print("DEAD_CELL :", DEAD_CELL)
        add_cells.sort(key=lambda x:x[1])
        add_cells.sort(key=lambda x:x[0])
        same_set, same_list = set(), []
        for idx in range(len(add_cells)-1):
            if add_cells[idx][0] == add_cells[idx+1][0] and add_cells[idx][1] == add_cells[idx+1][1]:
                same_set.add(idx)
                same_set.add(idx+1)
            else:
                if same_set: same_list.append(same_set)
                same_set = set()
        if same_set: same_list.append(same_set)
        for same in same_list[::-1]:
            MIN_IDX, MAX_IDX = min(same), max(same)
            MAX = max([item[2] for item in add_cells[MIN_IDX:MAX_IDX+1]])
            add_cells = add_cells[:MIN_IDX]+[[add_cells[MIN_IDX][0], add_cells[MIN_IDX][1], MAX, MAX, MAX]] + add_cells[MAX_IDX+1:]
        print("add_cells:", add_cells)
        for item in add_cells:
            if [item[0],item[1]] not in DEAD_CELL: CELL.append(item)
        print("CELL:", CELL)
        time += 1
        print("time : ", time, len(CELL), CELL)
        print()
    print("#{} {}".format(_+1, len(CELL)))
'''        
        
"""
# T = int(input())
DIR = [[-1,0],[1,0],[0,-1],[0,1]]
T = 1
for _ in range(T):
    # N,M,K = map(int, input().split())
    N,M,K = 2,2,10
    # MAP = [list(map,int(input().spllit())) for i in range(N)]
    # MAP = [[3,2,0,3,0],[0,3,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,2]]
    MAP=[[1,1],[0,2]]
    CELL, DEAD_CELL = [], []
    for col in range(N):
        for row in range(N):
            if MAP[col][row] != 0: CELL.append([col,row,MAP[col][row],MAP[col][row]])
    # print("ORIGIN", CELL)
    time = 0
    
    while time <= K-1:
        add_cells, remove_cells = [], []
        CELL_POINT = [[item[0],item[1]] for item in CELL]
        for idx, item in enumerate(CELL):
            if item[3] == 0:
                for y, x in DIR:
                    if [y+item[0], x+item[1]] not in CELL_POINT and [y+item[0], x+item[1]] not in DEAD_CELL: add_cells.append([y+item[0], x+item[1], item[2], item[2]])
                remove_cells.append(idx)
            else: CELL[idx][3] -= 1
        
        # print("BEFORE CELL:", CELL)
        # print("remove_cells :", remove_cells)
        
        for idx in remove_cells[::-1]:
            item = CELL.pop(idx)
            DEAD_CELL.append([item[0], item[1]])
        # print("CELL:", CELL)
        # print("DEAD_CELL :", DEAD_CELL)
        add_cells.sort(key=lambda x:x[1])
        add_cells.sort(key=lambda x:x[0])
        same_set, same_list = set(), []
        for idx in range(len(add_cells)-1):
            if add_cells[idx][0] == add_cells[idx+1][0] and add_cells[idx][1] == add_cells[idx+1][1]:
                same_set.add(idx)
                same_set.add(idx+1)
            else:
                if same_set: same_list.append(same_set)
                same_set = set()
        if same_set: same_list.append(same_set)
        for same in same_list[::-1]:
            MIN_IDX, MAX_IDX = min(same), max(same)
            MAX = max([item[2] for item in add_cells[MIN_IDX:MAX_IDX+1]])
            add_cells = add_cells[:MIN_IDX]+[[add_cells[MIN_IDX][0], add_cells[MIN_IDX][1], MAX, MAX]] + add_cells[MAX_IDX+1:]
        # print("add_cells:", add_cells)
        for item in add_cells:
            if [item[0],item[1]] not in DEAD_CELL: CELL.append(item)
        # print("CELL:", CELL)
        time += 1
        # print("time : ", time, len(CELL), CELL)
        # print()
    print("#{} {}".format(_+1, len(CELL)))
        
"""        