def isarr(r, c):
    return True if 0<=r<N and 0<=c<M else False
 
def BFS(r, c, d):
    queue = []
    visited[r][c] = 1
    queue.append([r,c])
    answer = 1
    while queue:
        y, x = queue.pop(0)
        for i in direction[arr[y][x]]:
            ny = y + i[0]
            nx = x + i[1]
            if isarr(ny, nx) and not visited[ny][nx]:
                if [-i[0], -i[1]] in direction[arr[ny][nx]]:
                    visited[ny][nx] = visited[y][x] + 1
                    if visited[ny][nx] > d:
                        return answer
                    answer += 1
                    queue.append([ny, nx])
    return answer
 
T = int(input())
for _ in range(T):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    visited = [[0]*M for i in range(N)]
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    direction = [[], 
        [d[0], d[1], d[2], d[3]], 
        [d[0], d[1]],
        [d[2], d[3]],
        [d[0], d[3]],
        [d[1], d[3]],
        [d[1], d[2]],
        [d[0], d[2]]    
        ]
    print(f"#{_+1} {BFS(R, C, L)}")
"""
_1 = [[1,0], [-1,0],[0,1], [0,-1]]
_2 = [[1,0], [-1,0]]
_3 = [[0,1], [0,-1]]
_4 = [[-1,0], [0,1]]
_5 = [[1,0], [0,1]]
_6 = [[1,0], [0,-1]]
_7 = [[-1,0], [0,-1]]

def bfs(arr, c, d, ans, depth, state, list1):
    if(depth == state):
        print("이제 끝냅시다")
        if (c,d) in list1:
            return
        else:
            if (arr[c][d] ==0):
                return
            else:
                list1.append((c,d))
            return
        # 그만 찾아요

    else:
        state += 1
        if (arr[c][d] == 0):
            state -= 1
            print("@@@@@@@@@@@@@@@@20으로 들어옴@@@@@@@@@@@@@@@@@@")
            return

        elif(arr[c][d] == 1):
            if (c,d) in list1:
                return
            else:
                list1.append((c,d))
                for arr1 in _1:
                    print("arr1 :",arr1)
                    print("c, d :"+str(c) + " " + str(d))
                    print(list1)
                    if (c+arr1[0], d+arr1[1]) in list1:
                        return
                    else:
                        bfs(arr,c+arr1[0], d+arr1[1], ans, depth, state, list1)

        elif(arr[c][d] == 2):
            if (c,d) in list1:
                return
            else:
                list1.append((c,d))
                for arr1 in _2:
                    print("arr1 :",arr1)
                    print("c, d :"+str(c) + " " + str(d))
                    print(list1)
                    if (c+arr1[0], d+arr1[1]) in list1:
                        return
                    else:
                        bfs(arr,c+arr1[0], d+arr1[1], ans, depth, state, list1)

        elif(arr[c][d] == 3):
            if (c,d) in list1:
                return
            else:
                list1.append((c,d))
                for arr1 in _3:
                    print("arr1 :",arr1)
                    print("c, d :"+str(c) + " " + str(d))
                    print(list1)
                    if (c+arr1[0], d+arr1[1]) in list1:
                        return
                    else:
                        bfs(arr,c+arr1[0], d+arr1[1], ans, depth, state, list1)
        
        elif(arr[c][d] == 4):
            if (c,d) in list1:
                return
            else:
                list1.append((c,d))
                for arr1 in _4:
                    print("arr1 :",arr1)
                    print("c, d :"+str(c) + " " + str(d))
                    print(list1)
                    if (c+arr1[0], d+arr1[1]) in list1:
                        return
                    else:
                        bfs(arr,c+arr1[0], d+arr1[1], ans, depth, state, list1)

        elif(arr[c][d] == 5):
            if (c,d) in list1:
                return
            else:
                list1.append((c,d))
                for arr1 in _5:
                    print("arr1 :",arr1)
                    print("c, d :"+str(c) + " " + str(d))
                    print(list1)
                    if (c+arr1[0], d+arr1[1]) in list1:
                        return
                    else:
                        bfs(arr,c+arr1[0], d+arr1[1], ans, depth, state, list1)

        elif(arr[c][d] == 6):
            if (c,d) in list1:
                return
            else:
                list1.append((c,d))
                for arr1 in _6:
                    print("arr1 :",arr1)
                    print("c, d :"+str(c) + " " + str(d))
                    print(list1)
                    if (c+arr1[0], d+arr1[1]) in list1:
                        return
                    else:
                        bfs(arr,c+arr1[0], d+arr1[1], ans, depth, state, list1)       

        elif(arr[c][d] == 7):
            if (c,d) in list1:
                return
            else:
                list1.append((c,d))
                for arr1 in _7:
                    print("arr1 :",arr1)
                    print("c, d :"+str(c) + " " + str(d))
                    print(list1)
                    if (c+arr1[0], d+arr1[1]) in list1:
                        return
                    else:
                        bfs(arr,c+arr1[0], d+arr1[1], ans, depth, state, list1)

T = int(input())
for _ in range(T):
    a, b, c, d, e = map(int, input().split())
    ans = 1
    arr= [[0]*b]*a
    
    for x in range(a):
        arr[x] = list(map(int, input().split()))
    print(arr)
    list1=[]
    bfs(arr, c, d, ans, e, 1, list1)
    #print("list : ",list1)
    print(f"#{_+1} {len(list1)}")
"""