#라스트 , visit 공유해서 터졌음 ㅠ
def CHECK(col):
    cnt, VISIT = 1, [True]*N
    for row in range(1,N):
        if MAP[col][row-1] == MAP[col][row]: cnt += 1
        elif MAP[col][row-1]+1 == MAP[col][row]:
            if cnt < X:return False
            for i in range(1,X+1): VISIT[row-i] = False
            cnt = 1
        elif MAP[col][row]-MAP[col][row-1] > 1: return False
    cnt = 1
    for row in range(N-2, -1, -1):
        if MAP[col][row] == MAP[col][row+1]: cnt += 1
        elif MAP[col][row] == MAP[col][row+1] + 1:
            if cnt < X:return False
            for i in range(1,X+1):
                if not VISIT[row+i]: return False
            cnt = 1
        elif MAP[col][row]-MAP[col][row+1] > 1: return False    
    return True
    
# T = int(input())
T = 1
for _ in range(T):
    # N,X = map(int,input().split())
    # N,X = 6, 2
    N,X = 15,3
    # MAP = [list(map(int,input().split())) for i in range(N)]
    # MAP = [[3,3,3,2,1,1],[3,3,3,2,2,1],[3,3,3,3,3,2],[2,2,3,2,2,2],[2,2,3,2,2,2],[2,2,2,2,2,2]]
    MAP = [[5, 4, 4, 3, 3, 3, 2, 2, 2, 3, 4, 4, 4, 4, 4], [5, 4, 4, 3, 3, 3, 2, 2, 2, 3, 4, 4, 4, 4, 4], [5, 5, 5, 5, 4, 4, 2, 2, 3, 4, 4, 4, 4, 4, 5], [5, 4, 4, 3, 3, 3, 2, 2, 3, 4, 4, 4, 4, 4, 4], [5, 3, 3, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4], [2, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 3], [2, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 3], [3, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 4, 4, 4], [5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4, 4, 5], [5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4, 4, 5], [5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 2, 2, 3, 3, 4], [5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 1, 2, 2, 3], [5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 1, 2, 2, 3]]
    answer = 0
    for idx in range(N):
        if CHECK(idx):answer += 1
    MAP = [list(item) for item in zip(*MAP)]
    for idx in range(N):
        if CHECK(idx):answer += 1
    print(answer)

"""
def construct(MAP):
    global answer
    for col in range(N):
        row_cnt, row_list, FLAG = 1, [], True
        for row in range(1, N):
            if MAP[col][row] - MAP[col][row-1] == 1:
                if row_cnt < X:
                    row_cnt, FLAG = 1, False
                    continue
                for cnt in range(1,X+1):row_list.append(row-cnt)
                row_cnt = 1
            elif MAP[col][row] - MAP[col][row-1] > 1:
                FLAG = False
                continue
            elif MAP[col][row] == MAP[col][row-1]: row_cnt += 1
        row_cnt = 1
        if FLAG:
            for row_r in range(N-2, -1, -1):
                if MAP[col][row_r]-MAP[col][row_r+1] == 1:     
                    if row_cnt < X:
                        row_cnt, FLAG = 1, False
                        continue
                    for cnt in range(1,X+1):
                        if row_r+cnt in row_list:
                            FLAG = False
                            continue
                    row_cnt = 1
                if not FLAG: continue
                elif MAP[col][row_r]-MAP[col][row_r+1] > 1:
                    FLAG = False
                    continue
                elif MAP[col][row_r] == MAP[col][row_r+1]: row_cnt += 1
        if FLAG: answer += 1

# T = int(input())
T = 1
for _ in range(T):
    # N,X = map(int, input())
    N,X = 6,2
    # MAP = [list(map(int, input().split())) for i in range(N)]
    MAP = [[3,3,3,2,1,1],[3,3,3,2,2,1],[3,3,3,3,3,2],[2,2,3,2,2,2],[2,2,3,2,2,2],[2,2,2,2,2,2]]
    MAP_TRANSPOSE = [list(x) for x in zip(*MAP)]
    answer = 0
    construct(MAP)
    construct(MAP_TRANSPOSE)
    print(answer)
"""