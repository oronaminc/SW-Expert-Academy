dir={0:[0,0],1:[-1,0],2:[0,1],3:[1,0],4:[0,-1]}

def move(pos,d):
    return [pos[0]+dir[d][0], pos[1]+dir[d][1]]

def charge(posA,posB, BC):
    charging=0
    ableA, ableB = [],[]
    for i in range(len(BC)):
        if abs(BC[i][0]-posA[0]) + abs(BC[i][1]-posA[1]) <= BC[i][2]:
            ableA.append(i)
        if abs(BC[i][0]-posB[0]) + abs(BC[i][1]-posB[1]) <= BC[i][2]:
            ableB.append(i)
    for i in ableA:
        for j in ableB:
            if i==j: tmp=BC[i][3]
            else: tmp = BC[i][3] + BC[j][3]
            if tmp>charging: charging = tmp
    if len(ableB)==0:
        for i in ableA:
            if BC[i][3] > charging : charging=BC[i][3]
    elif len(ableA)==0:
        for i in ableB:
            if BC[i][3] > charging : charging=BC[i][3]
    return charging
    
T = int(input())
for _ in range(T):
    ans = 0
    M,A = map(int,input().split())
    move_A = list(map(int, input().split()))
    move_B = list(map(int, input().split()))
    posA, posB = [0,0], [9,9]
    BC=[]
    for i in range(A):
        BC.append(list(map(int,input().split())))
        BC[-1][0],BC[-1][1] = BC[-1][1]-1, BC[-1][0]-1
    for j in range(M):
        ans += charge(posA, posB, BC)
        posA = move(posA, move_A[j])
        posB = move(posB, move_B[j])
    ans += charge(posA, posB, BC)
    print(f'#{_+1} {ans}')


