from itertools import combinations
def CHECK_row(MAP,row):
    if K==1: return True
    cnt = 1
    for col in range(1,D):
        if MAP[col][row] == MAP[col-1][row]: cnt += 1
        else: cnt = 1
        if cnt >= K: return True
    return False
def CHECK(MAP):
    for idx in range(W):
        if not (CHECK_row(MAP, idx)): return False
    return True
def DFS(MAP, item):
    global FLAG
    if not item:
        if CHECK(MAP): FLAG = True
        return
    for change_val in range(2):
        MAP_COPY = [item[:] for item in MAP]
        MAP_COPY[item[0]] = [change_val]*W
        DFS(MAP_COPY, item[1:])
T = 1
# T = int(input())
for _ in range(T):
    # D,W,K = map(int,input().split())
    D,W,K = 6,8,3
    # MAP = [list(map(int,input().split())) for i in range(D)]
    MAP = [[0, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 1, 1, 1], [0, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 1],[0, 1, 1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 1, 1, 0, 1]]
    total, FLAG = range(D), False
    if CHECK(MAP): print("#{} {}".format(_+1,0))
    else:
        for idx in range(1,D+1):
            for item in combinations(total,idx):
                DFS(MAP, item)
                if FLAG: break
            if FLAG: break
        print("#{} {}".format(_+1,idx))

















"""
from itertools import combinations
def check_col(row, MAP):
    cnt = 1
    for col in range(D-1):
        if MAP[col][row] == MAP[col+1][row]:
            cnt +=1
            if cnt >= K:return True
        else:cnt=1
    if cnt >= K: return True
    return False
    
def check(MAP):
    for row in range(W):
        if not check_col(row, MAP): return False
    return True
            
# T = int(input())
T = 1
for _ in range(T):
    # D,W,K = map(int,input().split())
    # D,W,K = 6,8,3
    # MAP = [[0, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 1, 1, 1], [0, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 1, 1, 0, 1]]
    # D,W,K = 5,1,5
    # D,W,K = 3,1,3
    D,W,K = 13,1,1
    # MAP= [[0], [0], [0], [0], [1]]
    # MAP = [[0], [0], [0]]
    MAP = [[1],[0],[1],[0],[1],[0],[1],[0],[1],[0],[1],[0],[1]]
    if check(MAP): print("#{} {}".format(_+1, 0))
    else:
        FLAG = False
        for k in range(1,K+1):
            for item in combinations(range(D), k):
                MAP_COPY1 = [item for item in MAP]
                MAP_COPY2 = [item for item in MAP]
                for idx in item: MAP_COPY1[idx] = [0]*W
                if check(MAP_COPY1):
                    FLAG = True
                    print("#{} {}".format(_+1, k))
                    break
                for idx in item: MAP_COPY2[idx] = [1]*W
                if check(MAP_COPY2):
                    FLAG = True
                    print("#{} {}".format(_+1, k))
                    break
            if FLAG: break
"""