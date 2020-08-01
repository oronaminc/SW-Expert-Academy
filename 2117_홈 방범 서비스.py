#LAST
# T = int(input())
T = 1
for _ in range(T):
    # N,M = map(int,input().split())
    N,M = 8,3
    # MAP = [list(map(int,input().split())) for i in range(N)]
    MAP = [[0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
    HOUSE, MAX = [],float('-inf')
    for col in range(N):
        for row in range(N):
            if MAP[col][row] == 1: HOUSE.append([col,row])  
    
    for k in range(1,2*N+2):
        for col in range(N):
            for row in range(N):
                house_cnt = 0
                for y,x in HOUSE:
                    if abs(col-y)+abs(row-x) < k: house_cnt += 1
                cost = 2*k*(k-1) + 1
                if (house_cnt*M)-cost >= 0 and MAX < house_cnt: MAX = house_cnt
    print(MAX)
                

"""
# T = int(input())
T = 1
for _ in range(T):
    # N, M = map(int, input().split())
    # N,M = 8,3
    # N,M = 15, 2
    # N,M = 3,1
    N,M = 15,3
    # MAP = [list(map(int, input().split())) for i in range(N)]
    # MAP = [[0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
    MAP = [[1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0], [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0], [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0]]
    # MAP=[[1,0,0],[0,0,0], [0,0,1]]
    MAP = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0]]
    HOUSE = []
    MAX_HOUSE = float('-inf')
    for item in MAP: print(item)
    for col in range(N):
        for row in range(N):
            if MAP[col][row] == 1: HOUSE.append([col, row])
    for K in range(1,N+2):
        for start_col in range(N):
            for start_row in range(N):
                house_cnt, house_list = 0, []
                for house_col, house_row in HOUSE:
                    if abs(start_col-house_col) + abs(start_row-house_row) < K:
                        house_list.append([house_col, house_row])
                        house_cnt += 1
                if house_cnt*M - (2*K*(K-1)+1) >= 0 and MAX_HOUSE < house_cnt:
                    MAX_HOUSE = house_cnt
                    print(house_list)
                    print("MAX", house_cnt, "K:", K, house_cnt*M, 2*K*(K-1)+1,  start_col, start_row)
    print(MAX_HOUSE)
"""