#마지막 풀이
# 앞으로 for문 뒤로 for문 쓰
# T = int(input())
T =1
for _ in range(T):
    # K = int(input())
    K = 2
    # WHEEL = [list(map(int, input().split())) for i in rnage(4)]
    WHEEL = [[0, 0, 1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 1, 0, 0], [0, 0, 1, 0, 1, 1, 0, 1]]
    # INFO = [list(map(int, input().split())) for i in range(K)]
    INFO = [[1,1],[3,-1]]
    # 오른쪽 검사 부터 만들어 보자
    print(WHEEL)
    answer = 0
    for idx, direction in INFO:
        MOVE = [[idx,direction]]
        idx -= 1
        for new_idx in range(3):
            if new_idx+idx+1 > 3: break
            if WHEEL[idx+new_idx][2]+WHEEL[idx+new_idx+1][6] == 1:
                MOVE.append([idx+new_idx+2,direction*((-1)**(new_idx+1))])
            else: break
                
        for new_idx in range(3):
            if idx-new_idx-1 < 0: break
            if WHEEL[idx-new_idx][6]+WHEEL[idx-new_idx-1][2] == 1: 
                MOVE.append([idx-new_idx,direction*((-1)**(new_idx+1))])
            else: break
        
        for move_idx, move_dir in MOVE:
            move_idx -= 1
            if move_dir==1: WHEEL[move_idx] = [WHEEL[move_idx][-1]]+WHEEL[move_idx][:-1]
            else: WHEEL[move_idx] = WHEEL[move_idx][1:]+[WHEEL[move_idx][0]]
    if WHEEL[0][0]:answer += 1
    if WHEEL[1][0]:answer += 2
    if WHEEL[2][0]:answer += 4
    if WHEEL[3][0]:answer += 8
    print(answer)
'''
wheel = [[0, 0, 1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 1, 0, 0], [0, 0, 1, 0, 1, 1, 0, 1]]
info = [[1, 1], [3, -1]]
w_set1, w_set2, w_set3, w_set4 = set(), set(), set(), set()
for idx, data in enumerate(zip(wheel[0], wheel[1], wheel[2], wheel[3])):
    x,y,z,w = data
    if x==1: w_set1.add(idx)
    if y==1: w_set2.add(idx)
    if z==1: w_set3.add(idx)
    if w==1: w_set4.add(idx)
wheel_list = [w_set1, w_set2, w_set3, w_set4]

for start_idx, direction in info:
    start_idx -= 1
    move, RIGHT_FLAG, LEFT_FLAG = [[start_idx,direction]], True, True
    for move_idx in range(1,4):
        if start_idx+move_idx <len(wheel_list) and RIGHT_FLAG:
            if ((6 in wheel_list[start_idx+move_idx]) and (2 not in wheel_list[start_idx+move_idx-1])) or ((6 not in wheel_list[start_idx+move_idx]) and (2 in wheel_list[start_idx+move_idx-1])):
                move.append([start_idx+move_idx, direction*((-1)**move_idx)])
            else: RIGHT_FLAG = False
        if start_idx-move_idx > -1 and LEFT_FLAG:
            if ((2 in wheel_list[start_idx-move_idx]) and (6 not in wheel_list[start_idx-move_idx+1])) or ((2 not in wheel_list[start_idx-move_idx]) and (6 in wheel_list[start_idx-move_idx+1])):
                move.append([start_idx-move_idx, direction*((-1)**move_idx)])
            else:LEFT_FLAG = False
    for mv_pos, mv_dir in move:
        temp = set()
        for item in wheel_list[mv_pos]:
            if item+mv_dir > 7: item_val = 0
            elif item+mv_dir < 0: item_val = 7
            else: item_val = item+mv_dir
            temp.add(item_val)
        wheel_list[mv_pos] = temp

answer = 0
for idx, w_set in enumerate(wheel_list):
    if 0 in w_set: answer += (2**idx)
print(answer)
'''     












'''
def score(arr):
    sco,x=0,1
    for i in arr:
        if i[0] == 1:
            sco += x
        x *= 2
    return sco

def switch(arr,num):
    if num == 1: arr.insert(0,arr.pop())
    else: arr.append(arr.pop(0))

def wheel(arr, info):
    for i in info:
        if i[0]==1:
            if arr[0][2] != arr[1][6]:
                if arr[1][2] != arr[2][6]:
                    if arr[2][2] != arr[3][6]:
                        switch(arr[3],i[1]*(-1))
                    switch(arr[2],i[1])
                switch(arr[1],i[1]*(-1))
            switch(arr[0],i[1])
        elif i[0]==2:
            if arr[1][6] != arr[0][2]:
                switch(arr[0], i[1]*(-1))
            if arr[1][2] != arr[2][6]:
                if arr[2][2] != arr[3][6]:
                    switch(arr[3], i[1])
                switch(arr[2], i[1]*(-1))
            switch(arr[1],i[1])
        elif i[0]==3:
            if arr[2][2] != arr[3][6]:
                switch(arr[3], i[1]*(-1))
            if arr[2][6] != arr[1][2]:
                if arr[1][6] != arr[0][2]:
                    switch(arr[0], i[1])
                switch(arr[1],i[1]*(-1))
            switch(arr[2],i[1])
        elif i[0]==4:
            if arr[2][2] != arr[3][6]:
                if arr[1][2] != arr[2][6]:
                    if arr[0][2] != arr[1][6]:
                        switch(arr[0],i[1]*(-1))
                    switch(arr[1],i[1])
                switch(arr[2],i[1]*(-1))
            switch(arr[3],i[1])
            
T = int(input())
for _ in range(T):
    K = int(input())
    arr=[list(map(int,input().split())) for i in range(4)]
    info = [list(map(int,input().split())) for i in range(K)]
    wheel(arr,info)
    ans = score(arr)
    print(f'#{_+1} {ans}')
    '''