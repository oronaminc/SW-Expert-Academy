"""
def dfs(t,pre_map) :
    global my_min
    global n,w,h
    if pre_map.count(0) >= h*w :
        my_min = 0
        return
    if t >= n :
        result = h*w - pre_map.count(0)
        if result < my_min :
            my_min = result
        return
    for i in range(w) :
        for j in range(h) :
            if pre_map[i + w*j] > 0 :
                temp2_map = pre_map[:]
                bomb(i + w*j,temp2_map)
                pull(temp2_map)
                dfs(t+1,temp2_map)
                break
def bomb(k,pre_map) :
    global w
    global h
    if pre_map[k] :
        if pre_map[k] == 1 :
            pre_map[k] = 0
        else :
            t = pre_map[k]-1
            pre_map[k] = 0
            for i in range(1,t+1) :
                if k % w + i < w:     
                    bomb(k+i,pre_map)
                if k % w - i >= 0:
                    bomb(k-i,pre_map)
                if k + i*w < w*h :
                    bomb(k+i*w,pre_map)
                if k-i*w >= 0 :
                    bomb(k-i*w,pre_map)
def pull(pre_map) :
    global w
    global h
    for k in range(h-1,-1,-1):
        for i in range(w):
            if pre_map[i+w*k] == 0:
                for t in range(k-1,-1,-1) :
                    if pre_map[i+w*t] > 0 :
                        pre_map[i+w*k] = pre_map[i+w*t]
                        pre_map[i+w*t] = 0
                        break                   
for _ in range(int(input())) : 
    n,w,h= list(map(int,input().split()))
    fst_map = []
    for i in range(h) :
        fst_map.extend(list(map(int,input().split())))
    #fst_map = [list(map(int,input().split())) for i in range(h)]
    print(fst_map)
    my_min = 9999
    dfs(0,fst_map)
    print(f'#{_+1} {my_min}')
"""


def deepcopy(arr):
    return [arr[i][:] for i in range(len(arr))]
 
def DFS(arr, depth): # DFS 모든경우를 다 따짐
    global MIN
    if(depth == 0):
        MIN = min(MIN, brick_num(arr))
    else:
        for i in range(1, W+1):
            arr2 = deepcopy(arr)
            brick_break(arr2,i)
            DFS(arr2, depth-1)
 
def brick_num(arr): # 벽돌 개수 세기
    num = 0
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if(arr[i][j] != 0):
                num = num + 1
    return num
 
def brick_arrange(arr): # 벽돌 정렬하기
    for i in range(H-1, 0, -1):
        for j in range(1, W+1):
            if(arr[i][j] != 0):
                p=i
                while(arr[p+1][j] == 0 and p<H):
                    arr[p+1][j] = arr[p][j]
                    arr[p][j] = 0
                    p = p+1
 
def brick_bomb(a,b,arr): # 터트리기
    if(arr[a][b] == 1):
        arr[a][b] = 0
    else:
        len = arr[a][b]
        arr[a][b] = 0
        for i in range(1,len):
            if a-i>0:
                if arr[a-i][b] !=0: brick_bomb(a-i,b,arr)
            if a+i < H+1:
                if arr[a+i][b] !=0: brick_bomb(a+i,b,arr)
            if b-i>0:
                if arr[a][b-i] != 0: brick_bomb(a,b-i,arr)
            if b+i < W+1:
                if arr[a][b+i] !=0: brick_bomb(a,b+i,arr)
 
def brick_break(arr,n): # 벽돌 꺠기
    for i in range(1,H+1):
        if(arr[i][n] != 0):
            brick_bomb(i,n,arr)
            brick_arrange(arr)
            break
 
T = int(input())
  
for _ in range(T):
    N, W, H = map(int, input().split())
    arr = [[0]*(W+2) for rows in range(H+2)]
 
    for i in range(1, H + 1): # 벽돌 입력
        inp = input().split()
        for j in range(1, W + 1):
            arr[i][j] = int(inp[j-1])
 
    MIN = 1000000000000000
    DFS(arr, N)
 
    print(f'#{_+1} {MIN}')