# T = int(input())
from itertools import combinations
T = 1
for _ in range(T):
    # N, M, C = map(int,input().split())
    # N,M,C = 4,2,13
    N,M,C = 3,3,10
    # honey = [list(map(int, input().split())) for i in range(N)]
    # honey = [[6,1,9,7],[9,8,5,8],[3,4,5,3],[8,2,6,7]]
    honey = [[7,2,9],[6,6,6],[5,5,7]]
    visited = [[0]*N for i in range(N)]
    answer = 0
    for __ in range(2):
        MAX, MAX_IDX = float('-inf'),[0,0]
        for col, h_col in enumerate(honey):
            for row in range(len(h_col)-M+1):
                temp_num ,temp_list= 0, honey[col][row:row+M]
                if 0 in temp_list: continue
                if sum(temp_list) <= C:
                    for idx in range(row, row+M):temp_num += honey[col][idx]*honey[col][idx]
                else:
                    temp_set = set()
                    for cnt in range(len(temp_list)-1, 0, -1):
                        for item in combinations(temp_list,cnt):
                            if sum(item) > C: continue
                            temp_num2 = 0
                            for item_val in item: temp_num2 += item_val*item_val
                            temp_set.add(temp_num2)
                    temp_num = max(temp_set)
                if MAX < temp_num: MAX, MAX_IDX = temp_num, [col, row]
        for i in range(M): honey[MAX_IDX[0]][MAX_IDX[1]+i] = 0
        answer += MAX
    print(answer)