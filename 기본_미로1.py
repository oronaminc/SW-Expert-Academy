DIR = [[-1,0],[1,0],[0,-1],[0,1]]

for _ in range(10):
    T = int(input())
    MAP = [[int(x) for x in input()] for i in range(16)]
    QUEUE, VISIT, FLAG = [], [[True] * 16 for i in range(16)], False
    for col_idx in range(16):
        for row_idx in range(16):
            if MAP[col_idx][row_idx] == 2:
                QUEUE.append([col_idx, row_idx])
                break
    while QUEUE:
        Y,X = QUEUE.pop(0)
        VISIT[Y][X] = False
        for y,x in DIR:
            if VISIT[Y+y][X+x] == True:
                if MAP[Y+y][X+x] == 0: QUEUE.append([Y+y, X+x])
                if MAP[Y+y][X+x] == 3:
                    FLAG = True
                    break
        if FLAG: break
    print("#{} {}".format(_+1, int(FLAG)))