DIR = [[0,0.5],[0,-0.5],[-0.5,0],[0.5,0]]
# T = int(input())
T = 1
for _ in range(T):
    # N = int(input())
    # N = 4
    # CELLS = [list(map(int,input())) for i in range(N)]
    CELLS = [[-1000,0,3,5],[1000,0,2,3],[0,1000,1,7],[0,-1000,0,9]]
    answer = 0
    for cnt in range(4000):
        DICT, NEW_CELLS = dict(), []
        for x,y,direction, val in CELLS:
            X,Y = x + DIR[direction][0], y + DIR[direction][1]
            DICT[(X,Y)] = DICT.get((X,Y),[]) + [[direction,val]]
        for key, item in DICT.items():
            if len(item)>1:
                answer += sum(x[1] for x in item)
            else: NEW_CELLS.append([key[0],key[1],item[0][0],item[0][1]])
        CELLS = NEW_CELLS
    print(answer)        

"""
DIR = [[0,0.5],[0,-0.5],[-0.5, 0],[0.5,0]]
# T = int(input())
T = 1
for _ in range(T):
    # N = int(input())
    N = 4
    # CELLS = [list(map(int, input().split())) for i in range(N)]
    CELLS = [[-1000,0,3,5],[1000,0,2,3],[0,1000,1,7],[0,-1000,0,9]]
    # 이동 후 DIC으로 옮김 / DIC에서 다시 합치고, CELLS로 나디 옮기기
    answer = 0
    for cnt in range(2000):
        DICT = dict()
        for y,x,direction, val in CELLS:
            Y,X = y+DIR[direction][0], x+DIR[direction][1]
            DICT[(X,Y)] = DICT.get((X,Y), []) + [[direction, val]]
        CELLS = []
        for key, item in DICT.items():
            if len(item) > 1: answer += sum(x[1] for x in item)
            else:
                if X<-1000 or X > 1000 or Y<-1000 or Y > 1000: continue
                else: CELLS.append([key[0], key[1], item[0][0], item[0][1]])
        if len(CELLS) <2: break
    print(answer)
 """   
    

"""
DIR=[[-1,0],[1,0],[0,-1],[0,1]]
# T = int(input())
T=1
for _ in range(T):
    #N = int(input())
    N = 4
    # INFO = [list(map(int, input().split())) for i in range(N)]
    INFO = [[-1000,0,3,5],[1000,0,2,3],[0,1000,1,7],[0,-1000,0,9]]
    MAP = [[[] for i in range(4000+3)] for i in range(4000+3)]
    answer = 0
    for y,x,direction, val in INFO:
        B_FLAG = False
        for col_idx, col in enumerate(MAP):
            for row_idx, row in enumerate(col):            
                Y, X = 2*y+2000+1, 2*x+2000+1
                if col_idx == Y and row_idx == X:
                    MAP[Y][X].append([direction,val,1])
                    B_FLAG = True
                    print(MAP[Y][X])
                    break
            if B_FLAG: break
                

    for cnt in range(4002):
        for col_idx, col in enumerate(MAP):
            for row_idx, row in enumerate(col):
                if row:
                    # 하나씩 움직이면서 그 전 점에 있었던 정보 지우기
                    for idx, item in enumerate(row):
                        direction, val, flag = item
                        if flag:
                            MAP[col_idx+DIR[direction][0]][row_idx+DIR[direction][1]].append([direction, val, 0])
                            MAP[col_idx][row_idx][idx] = [-1,-1,0]
                    ERASE_IDX = []
                    for idx, item in enumerate(row):
                        if item[0] == -1: ERASE_IDX.append(idx)
                    for idx in ERASE_IDX[::-1]: MAP[col_idx][row_idx].pop(idx)
        
        ERASE_IDX = []
        for col_idx, col in enumerate(MAP):
            for row_idx, row in enumerate(col):
                if row:
                    # 겹쳐 있는 부분 없애기 and[ 끝에 걸쳐 있는데 DIR이 같으면 없애버리기 and 다시 1로 활성화 시키기]
                    if len(row) == 1:
                        if col_idx == 0 and row[0]==0:MAP[col_idx][row_idx] = []
                        elif col_idx == 4002 and row[0]==1:MAP[col_idx][row_idx] = []
                        elif row_idx == 0 and row[0]==2:MAP[col_idx][row_idx] = []
                        elif row_idx==4002 and row[0]==3: MAP[col_idx][row_idx] = []
                        else:MAP[col_idx][row_idx][0][2] = 1                    
                    elif len(row) > 1:
                        for item in row: answer += row[1]
                        MAP[col_idx][row_idx] = []
        for col_idx, col in enumerate(MAP):
            for row_idx, row in enumerate(col):
                if row:
                    print([col_idx, row_idx])
        print()
        

    print(answer)
                
    
"""