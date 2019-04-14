'''
def judge(runway,X):
    pos,n =1,len(runway)
    for i in range(n):
        runway[i] = [runway[i],0]
    tmp = [runway[0][0],1]
    while pos < n:
        if runway[pos][0] == tmp[0] and runway[pos][1] == 0:    #같은 높이, 계단 미설치인 경우
            tmp[1] += 1
        elif runway[pos][0] == tmp[0]+1:    #내가 1 더 클때
            if tmp[1] >= X: #그래도 계단 둘 수 있음
                for i in range(pos-1,pos-1-X,-1):   #계단 설치했다고 표시
                    runway[i][1]=1
                tmp=[runway[pos][0],1]
            else:   return False   #계단 못놔...
        elif runway[pos][0] > tmp[0]+1: return False    #한번에 2계단이상 못올려
        elif runway[pos][0] < tmp[0]:   #오히려 계단이 낮아지면? 일단 그냥 지나가
            if runway[pos][1] == 0: tmp=[runway[pos][0],1]  #계단 미설치면 1
            else:   tmp=[runway[pos][0],0]          #이미 설치되어있으면 0
        pos += 1

    runway.reverse()    #이제 반대로 가보자
    pos,tmp = 1,[runway[0][0],1-runway[0][1]]
    while pos < n:
        if runway[pos][0] == tmp[0] and runway[pos][1] == 0:    #같은 높이, 계단 미설치인 경우
            tmp[1] += 1
        elif runway[pos][0] == tmp[0] and runway[pos][1] == 1:  #같은높이지만, 이미 전에 계단 설치된 경우
            tmp[1] = 0
        elif runway[pos][0] == tmp[0]+1:    #내가 1 더 클때
            if tmp[1] >= X: #그래도 계단 둘 수 있음
                for i in range(pos-1,pos-1-X,-1):   #계단 설치했다고 표시
                    runway[i][1]=1
                if runway[pos][1] != 1: tmp=[runway[pos][0],1]
                else:   tmp=[runway[pos][0],0]
            else:   return False   #계단 못놔...
        elif runway[pos][0] > tmp[0]+1: return False    #한번에 2계단이상 못올려
        elif runway[pos][0] < tmp[0]:   #오히려 계단이 낮아지면? 일단 그냥 지나가
            if runway[pos][1] == 0: tmp=[runway[pos][0],1]  #계단 미설치면 1
            else:   tmp=[runway[pos][0],0]          #이미 설치되어있으면 0
        pos += 1
    return True


T = int(input())
for _ in range(T):
    answer=0
    N,X = map(int, input().split())
    board=[]
    for n in range(N):
        board.append(list(map(int,input().split())))
    for b in board:
        if judge(b[:],X):   answer+=1
    for col in range(N):
        temp=[]
        for row in range(N):
            temp.append(board[row][col])
        if judge(temp,X):   answer+=1
    print(f'#{_+1} {answer}')
'''
def row(arr):
    ans=0
    visited=[[0]*N for i in range(N)]
    for i in range(N):
        ready=1
        flag=True
        for j in range(N-1):
            if arr[i][j] > arr[i][j+1]: continue
            elif arr[i][j] == arr[i][j+1]: ready+=1
            elif arr[i][j] == arr[i][j+1] - 1:
                if ready >= X:
                    for k in range(j, j-X, -1):
                        visited[i][k] = 1
                    ready=1
                else:
                    flag=False
                    break
            else:
                flag=False
                break
        ready=1
        for j in range(N-1,0,-1):
            if arr[i][j] > arr[i][j-1]: continue
            elif arr[i][j] == arr[i][j-1]: ready +=1
            elif arr[i][j] == arr[i][j-1] -1:
                if ready >= X:
                    for k in range(j,X+j):
                        if visited[i][k]==1:
                            flag=False
                            break
                        else: visited[i][k] = 1
                    ready=1
                else:
                    flag=False
                    break
            else:
                flag=False
                break
        if flag: ans +=1
    return ans

def col(arr):
    ans=0
    visited=[[0]*N for i in range(N)]
    for i in range(N):
        ready=1
        flag=True
        for j in range(N-1): 
            if arr[j][i] > arr[j+1][i]: continue
            elif arr[j][i] == arr[j+1][i]:  ready+=1
            elif arr[j][i] == arr[j+1][i] - 1:
                if ready >= X:
                    for k in range(j, j-X, -1):
                        visited[k][i] = 1
                    ready=1
                else:
                    flag=False
                    break
            else:
                flag=False
                break
        ready=1
        for j in range(N-1,0,-1):
            if arr[j][i] > arr[j-1][i]: continue
            elif arr[j][i] == arr[j-1][i]: ready +=1
            elif arr[j][i] == arr[j-1][i] -1:
                if ready >= X:
                    for k in range(j,X+j):
                        if visited[k][i]==1:
                            flag=False
                            break
                        else: visited[k][i] = 1
                    ready=1
                else:
                    flag=False
                    break
            else:
                flag=False
                break
        if flag:  ans +=1
    return ans

T = int(input())
for _ in range(T):
    N,X=map(int,input().split())
    arr=[list(map(int,input().split())) for i in range(N)]
    ans=row(arr)+col(arr)
    print(f'#{_+1} {ans}')