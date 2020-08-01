#라스
def CHARGE():
    global answer
    a_list, b_list = [], []
    for idx, item in enumerate(BC):# 충전 여부 확인하기
        x,y,area,charge  = item
        if abs(A_POS[0]-x)+abs(A_POS[1]-y) <= area: a_list.append(idx)
        if abs(B_POS[0]-x)+abs(B_POS[1]-y) <= area: b_list.append(idx)
    
    if a_list or b_list:
        MAX = float('-inf')
        for x_idx in a_list:
            for y_idx in b_list:
                if x_idx == y_idx:
                    if MAX < BC[x_idx][3]: MAX = BC[x_idx][3]
                else:
                    if MAX < BC[x_idx][3] + BC[y_idx][3]: MAX = BC[x_idx][3] + BC[y_idx][3]
        if not b_list:
            if MAX < max([BC[idx][3] for idx in a_list]): MAX = max([BC[idx][3] for idx in a_list])
        if not a_list:
            if MAX < max([BC[idx][3] for idx in b_list]): MAX = max([BC[idx][3] for idx in b_list])
        answer += MAX

DIR = [[0,0],[0,-1],[1,0],[0,1],[-1,0]]
# T = int(input())
T= 1
for _ in range(T):
    # M,A = map(int, input().split())
    M,A = 20, 3
    # A_PERSON = list(map(int,input().split()))
    # B_PERSON = list(map(int,input().split()))
    A_PERSON = [2, 2, 3, 2, 2, 2, 2, 3, 3, 4, 4, 3, 2, 2, 3, 3, 3, 2, 2, 3]
    B_PERSON = [4, 4, 1, 4, 4, 1, 4, 4, 1, 1, 1, 4, 1, 4, 3, 3, 3, 3, 3, 3]
    # BC = [list(map(int,input().split())) for i in range(A)]
    BC = [[4,4,1,100],[7,10,3,40],[6,3,2,70]]
    A_POS, B_POS, answer = [1,1], [10,10], 0
    
    CHARGE()    
    for a,b in zip(A_PERSON, B_PERSON):
        A_POS[0], A_POS[1], B_POS[0], B_POS[1] = A_POS[0]+DIR[a][0], A_POS[1]+DIR[a][1], B_POS[0]+DIR[b][0], B_POS[1]+DIR[b][1]
        CHARGE()
        
    print(answer)
        
'''
dir={0:[0,0],1:[-1,0],2:[0,1],3:[1,0],4:[0,-1]}
def move(pos, d):
    return [pos[0]+dir[d][0],pos[1]+dir[d][1]]

def charge(posA,posB,AP):
    charging=0
    ableA,ableB=[],[]
    for i in range(len(AP)):
        if abs(AP[i][0]-posA[0])+abs(AP[i][1]-posA[1]) <= AP[i][2]: #A가 충전범위 안에 있으면
            ableA.append(i)
        if abs(AP[i][0]-posB[0])+abs(AP[i][1]-posB[1]) <= AP[i][2]: #B가 충전범위 안에 있으면
            ableB.append(i)
    for i in ableA:
        for j in ableB:
            if i==j:    tmp=AP[i][3]
            else:   tmp=AP[i][3]+AP[j][3]
            if tmp > charging:  charging = tmp
    if len(ableB)==0:
        for i in ableA:
            if AP[i][3] > charging: charging=AP[i][3]
    elif len(ableA)==0:
        for i in ableB:
            if AP[i][3] > charging: charging=AP[i][3]
    return charging

# T = int(input())
T = 1
for _ in range(T):
    answer = 0
    # M,A = map(int, input().split())
    # A_move = list(map(int, input().split()))
    # B_move = list(map(int, input().split()))
    M, A = 20, 3
    A_move = [2, 2, 3, 2, 2, 2, 2, 3, 3, 4, 4, 3, 2, 2, 3, 3, 3, 2, 2, 3]
    B_move = [4, 4, 1, 4, 4, 1, 4, 4, 1, 1, 1, 4, 1, 4, 3, 3, 3, 3, 3, 3]
    posA, posB= [0,0],[9,9]
    AP=[]
    for a in range(A):
        AP.append(list(map(int,input().split())))
        AP[-1][0],AP[-1][1]=AP[-1][1]-1,AP[-1][0]-1 #아 이거 바뿨줘야되네
    for i in range(M):
        answer += charge(posA,posB,AP)
        posA= move(posA,A_move[i])  #이동
        posB= move(posB,B_move[i])
    answer += charge(posA, posB, AP)
    print(f'#{_+1} {answer}')
'''
# T = int(input())

"""

def charge(A_pos, B_pos, AP):
    A, B, charging = set(), set(), 0
    for idx, item in enumerate(AP):
        x,y,r,charge = item
        if abs(A_pos[0]-x) + abs(A_pos[1]-y) <= r: A.add(idx)
        if abs(B_pos[0]-x) + abs(B_pos[1]-y) <= r: B.add(idx)
    for a in A:
        for b in B:
            if a==b:temp = AP[a][3]
            else: temp = AP[a][3]+AP[b][3]
            if charging < temp: charging = temp
    if not len(B):
        for a in A:
            if AP[a][3] > charging : charging = AP[a][3]
    if not len(A):
        for b in B:
            if AP[b][3] > charging : charging = AP[b][3]
    return charging
        
    

DIR={0:[0,0],1:[0,-1],2:[1,0],3:[0,1],4:[-1,0]}
T = 1
for _ in range(T):
    M,A,ans = 20,3,0
    # M, A = map(int, input().split())
    A_move = [2, 2, 3, 2, 2, 2, 2, 3, 3, 4, 4, 3, 2, 2, 3, 3, 3, 2, 2, 3]
    B_move = [4, 4, 1, 4, 4, 1, 4, 4, 1, 1, 1, 4, 1, 4, 3, 3, 3, 3, 3, 3]
    AP = [[4,4,1,100],[7,10,3,40],[6,3,2,70]]
    A_pos, B_pos = [1,1], [10,10]
    ans += charge(A_pos, B_pos, AP)
    for idx in range(M):
        A_pos[0], A_pos[1] = A_pos[0]+DIR[A_move[idx]][0], A_pos[1]+DIR[A_move[idx]][1]
        B_pos[0], B_pos[1] = B_pos[0]+DIR[B_move[idx]][0], B_pos[1]+DIR[B_move[idx]][1]
        ans += charge(A_pos, B_pos, AP)
    print(ans)
"""
"""
def charge(A_pos, B_pos, AP):
    A, B, charging = set(), set(), 0
    for idx, item in enumerate(AP):
        x,y,r,charge = item
        if abs(A_pos[0]-x) + abs(A_pos[1]-y) <= r: A.add(idx)
        if abs(B_pos[0]-x) + abs(B_pos[1]-y) <= r: B.add(idx)
    for a in A:
        for b in B:
            if a==b:temp = AP[a][3]
            else: temp = AP[a][3]+AP[b][3]
            if charging < temp: charging = temp
    if not len(B):
        for a in A:
            if AP[a][3] > charging : charging = AP[a][3]
    if not len(A):
        for b in B:
            if AP[b][3] > charging : charging = AP[b][3]
    return charging
        
DIR={0:[0,0],1:[0,-1],2:[1,0],3:[0,1],4:[-1,0]}
T = int(input())
for _ in range(T):
    M, A = map(int, input().split())
    A_move = list(map(int, input().split()))
    B_move = list(map(int, input().split()))
    AP = [0]*A 
    for a in range(A):	AP[a] = list(map(int,input().split()))
    A_pos, B_pos, ans = [1,1], [10,10], 0
    ans += charge(A_pos, B_pos, AP)
    for idx in range(M):
        A_pos[0], A_pos[1] = A_pos[0]+DIR[A_move[idx]][0], A_pos[1]+DIR[A_move[idx]][1]
        B_pos[0], B_pos[1] = B_pos[0]+DIR[B_move[idx]][0], B_pos[1]+DIR[B_move[idx]][1]
        ans += charge(A_pos, B_pos, AP)
    print("#{} {}".format(_+1,ans))
"""