from sys import stdin

move=[[1, 1], [1, -1], [-1, -1], [-1, 1]]
num = int(input())
for _ in range(num):
    N = int(input())
    arr = [list(map(int, stdin.readline().split())) for i in range(N)]
 
    ans = -1
    # 초기 점 설정
    for i in range(N-2):
        for j in range(1, N-1):
            y, x = i, j
            move_num = []
            for a in range(1, x+1):
                for b in range(1, N-x):
                    if b+a < N-y:
                        move_num.append([b, a])
                        continue

            print(move_num)
            print("x y :" + str(x) + " " + str(y))
            for a in move_num:
                new_l = []
                flag = 0
                for b in range(a[0]):
                    y += move[0][0]
                    x += move[0][1]
                    if arr[y][x] in new_l:
                        flag = 1
                    new_l.append(arr[y][x])
                    print("move 1 : ", new_l)
                for b in range(a[1]):
                    y += move[1][0]
                    x += move[1][1]
                    if arr[y][x] in new_l:
                        flag = 1
                    new_l.append(arr[y][x])
                    print("move 2 : ", new_l)
                for b in range(a[0]):
                    y += move[2][0]
                    x += move[2][1]
                    if arr[y][x] in new_l:
                        flag = 1
                    new_l.append(arr[y][x])
                    print("move 3 : ", new_l)
                for b in range(a[1]):
                    y += move[3][0]
                    x += move[3][1]
                    if arr[y][x] in new_l:
                        flag = 1
                    new_l.append(arr[y][x])
                    print("move 4 : " , new_l)
                if not flag:
                    ans = max((a[0] + a[1]) * 2, ans)
    print(f"#{_+1} {ans}")