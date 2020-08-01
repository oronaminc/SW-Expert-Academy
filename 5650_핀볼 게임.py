#상하좌우
DIR = [[-1,0],[1,0],[0,-1],[0,1]]
BLOCK = {1:[[1,0],[0,1],[-1,0],[0,-1]], 2:[[0,1],[-1,0],[1,0],[0,-1]], 3:[[0,-1],[-1,0],[0,1],[1,0]], 4:[[1,0], [0,-1],[0,1],[-1,0]], 5:[[1,0],[-1,0],[0,1],[0,-1]]}
# T = int(input())
T = 1
for _ in range(T):
    # N = int(input())
    N = 10
    # MAP = [list(map(int,input().split())) for i in range(N)]
    MAP = [[0, 1, 0, 3, 0, 0, 0, 0, 7, 0], [0, 0, 0, 0, -1, 0, 5, 0, 0, 0], [0, 4, 0, 0, 0, 3, 0, 0, 2, 2], [1, 0, 0, 0, 1, 0, 0, 3, 0, 0], [0, 0, 3, 0, 0, 0, 0, 0, 6, 0], [3, 0, 0, 0, 2, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 4, 0], [0, 5, 0, 4, 1, 0, 7, 0, 0, 5], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [2, 0, 6, 0, 0, 4, 0, 0, 0, 4]]
    HOLE, MAX = dict(), float('-inf')
    for col in range(N):
        for row in range(N):
            if MAP[col][row] > 5: HOLE[MAP[col][row]] = HOLE.get(MAP[col][row], [])+[[col,row]]
    print(HOLE)
    POINT = [2,3]
    direction = 3
    # POINT = [6,3]
    init_y, init_x = 2,3
    # direction = 2
    for col in range(N):
        for row in range(N):
            if MAP[col][row] == 0:
                print(">>", col, row)
                for direction in range(4):
                    POINT = [col,row]
                    init_y, init_x = col,row
                    answer = 0
                    while True:
                        new_y, new_x = POINT[0]+DIR[direction][0], POINT[1]+DIR[direction][1]            
                        if new_y<0 or new_y >=N or new_x<0 or new_x>=N:
                            answer += 1
                            direction  = direction + 1 if direction %2 == 0 else direction -1
                        elif 1<=MAP[new_y][new_x]<=5:
                            # print("??",  direction, DIR.index(BLOCK[MAP[new_y][new_x]][direction]), BLOCK[MAP[new_y][new_x]][direction])
                            answer += 1
                            direction = DIR.index(BLOCK[MAP[new_y][new_x]][direction])
                        elif 6<=MAP[new_y][new_x]<=10:
                            idx = 1- HOLE[MAP[new_y][new_x]].index([new_y,new_x])
                            new_y, new_x = HOLE[MAP[new_y][new_x]][idx]
                        if new_y == init_y and new_x == init_x: break
                        # print(new_y, new_x)
                        if 0<=new_y<N and 0<=new_x<N and MAP[new_y][new_x] == -1: break
                        POINT = [new_y,new_x]
                    # print(answer)
                    if MAX<answer: MAX = answer  
    print(MAX)
"""
DIR = [[-1,0],[1,0],[0,-1],[0,1]]
first = [[1,0],[0,1],[-1,0],[0,-1]]
second = [[0,1],[-1,0],[1,0],[0,-1]]
third = [[0,-1],[-1,0],[0,1],[1,0]]
fourth = [[1,0], [0,-1], [0,1],[-1,0]]
fifth = [[1,0],[-1,0],[0,1],[0,-1]]
SHAPE = [[],first, second, third, fourth, fifth]
# T = int(input())
T = 1
for _ in range(T):
    # N = int(input())
    # MAP = [list(map(int,input().split())) for i in range(N)]
    N = 4
    MAP = [[0,0,0,3],[0,0,0,0],[1,0,0,4],[0,0,0,0]]
    MAX = 0
    
    BLOCK, HOLE, START = [], [], []
    BLOCK_MAP, HOLE_MAP, BLACK_HOLE_MAP = [[False] * N for i in range(N)], [[False] * N for i in range(N)], [[False] * N for i in range(N)]
    WARM_HOLE_DICT ={}
        
    for col in range(N):
        for row in range(N):
            if 6<=MAP[col][row]<=10: WARM_HOLE_DICT[MAP[col][row]] = WARM_HOLE_DICT.get(MAP[col][row],[]) + [[col,row]]

    for start_y in range(N):
        for start_x in range(N):
            if MAP[start_y][start_x] == 0 and start_y==0 and start_x==1:
                
                for idx in range(4):
                    y,x = start_y, start_x
                    count = 0
                    print("idx===============", idx, y, x)
                    while True:
                        y,x = y+DIR[idx][0], x+DIR[idx][1]
                        print(">>>", y,x,idx,count)
                        if y == start_y and x== start_x: break                
                        elif 0<=x<N and 0<=y<N and MAP[y][x] == -1:break
                        elif y < 0 or y >=N or x < 0 or x >= N:
                            idx = idx-1 if idx%2==1 else idx + 1
                            count += 1
                        elif 1<=MAP[y][x]<=5:
                            idx = DIR.index(SHAPE[MAP[y][x]][idx])
                            count += 1
                        elif 6<=MAP[y][x]<=10:
                            if y == WARM_HOLE_DICT[MAP[y][x]][0][0] and x == WARM_HOLE_DICT[MAP[y][x]][0][1]:
                                y, x = WARM_HOLE_DICT[MAP[y][x]][1][0], WARM_HOLE_DICT[MAP[y][x]][1][1]
                            else: y, x = WARM_HOLE_DICT[MAP[y][x]][0][0], WARM_HOLE_DICT[MAP[y][x]][0][1]            
                        
                    if MAX < count: 
                        print(start_y, start_x,idx, count)
                        MAX = count
    print("#{} {}".format(_+1,MAX))
       
        
        
"""  
        
'''
    # print(WARM_HOLE_DICT)
    # for item in MAP: print(item)
    for start_x, start_y in START:
        y,x = start_y, start_x
        for idx in range(4):
            count = 0
            while True:
                y,x = y+DIR[idx][0], x+DIR[idx][1]
                
                if y == start_y and x== start_x: break                
                elif 0<=x<N and 0<=y<N and MAP[y][x] == -1:break
                elif y < 0 or y >=N or x < 0 or x >= N:
                    idx = idx-1 if idx%2==1 else idx + 1
                    count += 1
                elif 1<=MAP[y][x]<=5:
                    idx = DIR.index(SHAPE[MAP[y][x]][idx])
                    count += 1
                elif 6<=MAP[y][x]<=10:
                    if y == WARM_HOLE_DICT[MAP[y][x]][0][0] and x == WARM_HOLE_DICT[MAP[y][x]][0][1]:
                        y, x = WARM_HOLE_DICT[MAP[y][x]][1][0], WARM_HOLE_DICT[MAP[y][x]][1][1]
                    else: y, x = WARM_HOLE_DICT[MAP[y][x]][0][0], WARM_HOLE_DICT[MAP[y][x]][0][1]            
                
            if MAX < count: MAX = count
        # break
    print(MAX)
    '''
    