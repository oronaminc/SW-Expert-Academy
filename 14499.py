
N,M,x,y,k = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]
order = list(map(int,input().split()))

dice = [0,0,0,0,0,0,0]
for order_num in order:
    if order_num == 1:
        if y == M-1: continue
        else:#2,5는 안움직여
            y+=1
            temp = dice[1]
            dice[1] = dice[4]
            dice[4] = dice[6]
            dice[6] = dice[3]
            dice[3] = temp                  
    elif order_num == 2:
        if y == 0: continue
        else:#2,5는 안움직여
            y-=1
            temp = dice[3]
            dice[3] = dice[6]
            dice[6] = dice[4]
            dice[4] = dice[1]
            dice[1] = temp
    elif order_num == 3:
        if x == 0: continue
        else:#3,4는 안움직여
            x-=1
            temp = dice[1]
            dice[1] = dice[5]
            dice[5] = dice[6]
            dice[6] = dice[2]
            dice[2] = temp
    elif order_num == 4:
        if x == N-1: continue
        else:#3,4는 안움직여
            x += 1
            temp = dice[2]
            dice[2] = dice[6]
            dice[6] = dice[5]
            dice[5] = dice[1]
            dice[1] = temp

    if arr[x][y] == 0:
        arr[x][y]  = dice[6]
    else:
        dice[6] = arr[x][y] 
        arr[x][y]  = 0
    print(dice[1])
"""

n, m, x, y, k = map(int, input().split())
world  = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))

dice = [0] * 7

move = [[0,1],[0,-1], [-1,0],[1,0]]

def valid(x,y,n,m):
    return not (x < 0 or x >= n or y < 0 or y >= m)

for dir in order :
    new_x = x + move[dir-1][0]
    new_y = y + move[dir-1][1]
    if valid(new_x, new_y,n,m):
        x, y = new_x, new_y
        if dir == 1:  # EAST
            dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]
        elif dir == 2:  # WEST
            dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]
        elif dir == 3:  # NORTH
            dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]
        elif dir == 4:  # SOUTH
            dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]
        if world[x][y] == 0:
            world[x][y] = dice[6]
        else :
            dice[6], world[x][y] = world[x][y], 0

        print(dice[1])
        """