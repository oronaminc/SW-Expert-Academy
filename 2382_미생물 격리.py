#라스
DIR = [[],[-1,0],[1,0],[0,-1],[0,1]]
# T = int(input())
T = 1
for _ in range(T):
    # N,M,K = map(int,input().split())
    N,M,K = 7,2,9
    # CELL = [list(map(int,input().split())) for i in range(K)]
    CELL = [[1, 1, 7, 1], [2, 1, 7, 1], [5, 1, 5, 4], [3, 2, 8, 4], [4, 3, 14, 1], [3, 4, 3, 3], [1, 5, 8, 2], [3, 5, 100, 1], [5, 5, 1, 1]]
    # 이동 -> 약품 -> DICT
    for __ in range(M):
        DICT, NEW_CELL = dict(), []
        for y,x,cnt,direction in CELL:
            Y,X = y+DIR[direction][0], x+DIR[direction][1]
            if X == 0 or X == N-1 or Y==0 or Y==N-1: 
                direction = direction+1 if direction%2==1 else direction -1
                cnt = cnt//2
            if cnt !=0: DICT[(Y,X)] = DICT.get((Y,X), [])+[[Y,X,cnt,direction]]
        for key, item in DICT.items():
            if len(item) > 1:
                new_direction = sorted(item, key=lambda x:x[2], reverse=True)[0][3]
                new_cnt = sum(x[2] for x in item)
                NEW_CELL.append([key[0],key[1],new_cnt,new_direction])
            else: NEW_CELL.append(item[0])
        CELL = NEW_CELL
    print(sum(x[2] for x in CELL))
"""
DIR = [[],[-1,0],[1,0],[0,-1],[0,1]]

# T = int(input())
T = 1
for _ in range(T):
    # N,M,K = map(int,input().split())
    # N,M,K = 7,4,9
    N,M,K = 10,8,19
    # CELL = [list(map(int,input().split())) for i in range(K)]
    # CELL = [[1, 1, 7, 1], [2, 1, 7, 1], [5, 1, 5, 4], [3, 2, 8, 4], [4, 3, 14, 1], [3, 4, 3, 3], [1, 5, 8, 2], [3, 5, 100, 1], [5, 5, 1, 1]]
    CELL = [[3, 1, 52, 4], [6, 8, 423, 3], [7, 3, 498, 4], [7, 5, 633, 3], [7, 7, 392, 3], [6, 6, 458, 4], [3, 8, 830, 3], [5, 1, 799, 3], [1, 1, 540, 3], [4, 8, 567, 3], [1, 6, 897, 3], [5, 4, 230,
1], [2, 6, 229, 3], [1, 5, 147, 1], [4, 1, 754, 2], [3, 3, 569, 1], [7, 8, 515, 4], [2, 4, 528, 4], [2, 1, 962, 2]]


    for item in CELL: print(item)
    
    for m in range(M):
        zero_list = []
        for idx, item in enumerate(CELL):
            y,x,cnt,direction = item
            y,x = y+DIR[direction][0], x+DIR[direction][1]
            if x==0 or x==N-1 or y==0 or y==N-1:
                cnt = cnt//2
                direction = direction - 1 if direction % 2 == 0 else direction + 1
            if cnt == 0: zero_list.append(idx)
            CELL[idx] = [y,x,cnt,direction]
        for idx in zero_list[::-1]: CELL.pop(idx)
        
        CELL = sorted(CELL, key=lambda x:x[1])
        CELL = sorted(CELL, key=lambda x:x[0])
        
        same_set, same_list = set(), []
        for idx in range(len(CELL)-1):
            if CELL[idx][0] == CELL[idx+1][0] and CELL[idx][1] == CELL[idx+1][1]:
                same_set.add(idx+1)
                same_set.add(idx)
            else:
                if same_set: same_list.append(same_set)
                same_set = set()
        if same_set: same_list.append(same_set)
        same_list = same_list[::-1]
        for item in same_list:
            max_idx, min_idx = max(item), min(item)
            TEMP_CELL = sorted(CELL[min_idx:max_idx+1], key=lambda x: x[2], reverse=True)
            print("TEMP_CELL", TEMP_CELL, max_idx, min_idx)
            new_direction = TEMP_CELL[0][3]
            new_cnt = sum(x[2] for x in TEMP_CELL)
            CELL = CELL[:min_idx]+[[CELL[min_idx][0], CELL[min_idx][1], new_cnt, new_direction]] + CELL[max_idx+1:]
            
        for item in CELL: print(item)
        print("LEN", len(CELL))
    print(sum(x[2] for x in CELL))
        
"""