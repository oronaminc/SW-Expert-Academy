T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
 
    point = []
    # 입구가 있는 좌표와 길이
    stair = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                point.append([i, j])
            if arr[i][j] > 1:
                stair.append([i, j, arr[i][j]])
    #첫번째 두번째 출구 비교
    dif = []
    for j in point:
        # 점에서 걸리는 총 거리를 나타냄
        time = []
        for i in stair:
            dis = abs(i[0]-j[0]) + abs(i[1]-j[1]) + 1
            time.append(dis + i[2])
        dif.append(time)

    res = []
    r1 = 0
    r2 = 0
    m_i = 0
    for i in dif:
        if i[0] < i[1]:
            r1 += 1
            res.append([i[0], 1, m_i])
        else:
            r2 += 1
            res.append([i[1], 2, m_i])
        m_i += 1
    res.sort()
    for i in res:
        if r1 > 3:
            #첫번째 거리 = min(첫 번째 계단의 길이 + 제일 빠른 dis, i번째 에 있었던 두번째 출구의 거리)
            i[0] = min(i[0]+stair[0][2], dif[i[2]][1])
            r1 -= 1
        if r2 > 3:
            i[0] = min(i[0]+stair[1][2], dif[i[2]][0])
            r2 -= 1
    r = 0
    for i in res:
        r = max(i[0], r)
    print(f"#{_+1} {r}")