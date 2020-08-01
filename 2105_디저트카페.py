#마지
def DFS(direction, point, SET, a, b):
    global MAX
    if direction >=4: return
    if direction >= 3 and a==0 and b==1:
         if MAX < len(SET): MAX = len(SET)
         return
    Y,X = point[0]+DIR[direction][0], point[1]+DIR[direction][1]
    if X<0 or X>=N or Y<0 or Y>=N:return
    if MAP[Y][X] in SET: return
    SET.append(MAP[Y][X])
    
    temp_SET = [item for item in SET]
    temp_a, temp_b = a, b
    temp_y, temp_x = Y,X
    if direction == 0: temp_a += 1
    if direction == 1: temp_b += 1
    if direction == 2: temp_a -= 1
    if direction == 3: temp_b -= 1
    DFS(direction, [temp_y,temp_x], temp_SET,temp_a,temp_b)
    temp_SET = [item for item in SET]
    temp_a, temp_b = a, b
    temp_y, temp_x = Y,X
    if direction == 0: temp_a += 1
    if direction == 1: temp_b += 1
    if direction == 2: temp_a -= 1
    if direction == 3: temp_b -= 1
    DFS(direction+1, [temp_y,temp_x], temp_SET,temp_a,temp_b)
    
DIR = [[1,1],[1,-1],[-1,-1],[-1,1]]
# T = int(input())
T = 1
for _ in range(T):
    # N = int(input())
    N = 4
    # MAP = [list(map(int, input().split())) for i in range(4)]
    MAP = [[9,8,9,8],[4,6,9,4],[8,7,7,8],[4,5,3,5]]
    MAX = float('-inf')
    for col in range(N-2):
        for row in range(1,N-1):
            DFS(0,[col,row], [MAP[col][row]], 0, 0)
    if MAX == float('-inf'): MAX = -1
    print("#{} {}".format(_+1, MAX))


"""
DIR = [[1,1],[1,-1],[-1,-1],[-1,1]]

def dfs(num_set, pnt, direction, count1, count2):
    global answer
    num_set.append(MAP[pnt[0]][pnt[1]])
    if direction == 3:
        if count1 == 0 and count2 == 0:
            # print(">>>", num_set, pnt, direction, count1, count2)
            answer += 1
            return
    
    Y1, X1 = pnt[0]+DIR[direction][0], pnt[1]+DIR[direction][1]
    num_set2 = [x for x in num_set]
    if 0<=X1<N and 0<=Y1<N:
        if direction == 3 or MAP[Y1][X1] not in num_set2:
            if direction == 0: count1 += 1
            elif direction == 1: count2 += 1
            elif direction == 2: count1 -= 1
            elif direction == 3: count2 -= 1
            if count1 >= 0 and count2 >= 0: dfs(num_set2, [Y1,X1], direction, count1, count2)
            if direction == 0: count1 -= 1
            elif direction == 1: count2 -= 1
            elif direction == 2: count1 += 1
            elif direction == 3: count2 += 1
    if direction+1 <=3:
        Y2, X2 = pnt[0]+DIR[direction+1][0], pnt[1]+DIR[direction+1][1]
        num_set2 = [x for x in num_set]
        if 0<=X2<N and 0<=Y2<N:
            if direction+1 == 3 or MAP[Y2][X2] not in num_set2:
                if direction+1 == 0: count1 += 1
                elif direction+1 == 1: count2 += 1
                elif direction+1 == 2: count1 -= 1
                elif direction+1 == 3: count2 -= 1
                if count1 >= 0 and count2 >= 0: dfs(num_set2, [Y2,X2], direction+1, count1, count2)
                if direction+1 == 0: count1 -= 1
                elif direction+1 == 1: count2 -= 1
                elif direction+1 == 2: count1 += 1
                elif direction+1 == 3: count2 += 1


def dfs(num_set, pnt, direction, count1, count2):
    global answer
    num_set.append(MAP[pnt[0]][pnt[1]])
    if direction == 3:
        if count1 == 0 and count2 == 0:
            print(">>>", num_set, pnt, direction, count1, count2)
            answer = max(answer, len(num_set)-1)
            return
    
    Y1, X1 = pnt[0]+DIR[direction][0], pnt[1]+DIR[direction][1]
    num_set2 = [x for x in num_set]
    if 0<=X1<N and 0<=Y1<N:
        if (direction == 3 and count2==1) or MAP[Y1][X1] not in num_set2:
            if direction == 0: count1 += 1
            elif direction == 1: count2 += 1
            elif direction == 2: count1 -= 1
            elif direction == 3: count2 -= 1
            if count1 >= 0 and count2 >= 0: dfs(num_set2, [Y1,X1], direction, count1, count2)
            if direction == 0: count1 -= 1
            elif direction == 1: count2 -= 1
            elif direction == 2: count1 += 1
            elif direction == 3: count2 += 1
    if direction+1 <=3:
        Y2, X2 = pnt[0]+DIR[direction+1][0], pnt[1]+DIR[direction+1][1]
        num_set2 = [x for x in num_set]
        if 0<=X2<N and 0<=Y2<N:
            if (direction+1 == 3 and count2 ==1) or MAP[Y2][X2] not in num_set2:
                if direction+1 == 0: count1 += 1
                elif direction+1 == 1: count2 += 1
                elif direction+1 == 2: count1 -= 1
                elif direction+1 == 3: count2 -= 1
                if count1 >= 0 and count2 >= 0: dfs(num_set2, [Y2,X2], direction+1, count1, count2)
                if direction+1 == 0: count1 -= 1
                elif direction+1 == 1: count2 -= 1
                elif direction+1 == 2: count1 += 1
                elif direction+1 == 3: count2 += 1

# T = int(input())
T = 1

for _ in range(T):
    # N = int(input())
    N = 6
    answer = -1
    # MAP = [list(map(int, input().split())) for i in range(N)]
    # MAP = [[9,8,9,8], [4,6,9,4], [8,7,7,8], [4,5,3,5]]
    MAP = [[1,8,9,6,3,9],[5,3,1,9,8,2],[6,9,3,4,1,2],[7,1,1,5,1,9],[1,9,6,8,7,3],[7,6,4,5,5,5]]
    for start_col in range(N-2):
        for start_row in range(1,N-1):
            num_set, count1, count2 = [], 0, 0
            dfs(num_set, [start_col, start_row], 0, 0, 0)
print(answer)

"""