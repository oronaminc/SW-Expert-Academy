def search(y,x,c,k,n):
    global maxx
    if maxx < c+1: maxx = c+1
    visited[y][x] = 1
    for i in range(4):
        dy, dx = y+[1,0,-1,0][i], x+[0,1,0,-1][i]
        if dy<0 or dx<0 or dy>=n or dx>=n:
            continue
        if visited[dy][dx] !=1:
            if arr[dy][dx] < arr[y][x]:
                search(dy, dx, c+1, k, n)
            elif arr[dy][dx]-k < arr[y][x]:
                pre = arr[dy][dx]
                arr[dy][dx] = arr[y][x]-1
                search(dy,dx,c+1,0,n)
                arr[dy][dx] = pre
    visited[y][x] = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(a)]
    visited = [[0]*a for i in range(a)]
    
    max_num = -1; max_arr=[]; 
    for __ in arr:
        max_arr.append(max(__))
    max_num = max(max_arr)

    maxx = -1; max_point=[]
    for x in range(a):
        for y in range(a):
            if(arr[x][y] == max_num):
                max_point.append([x,y])

    for point in max_point:
        search(point[0], point[1], 0, b, a)
    print(f"#{_+1} {maxx}")