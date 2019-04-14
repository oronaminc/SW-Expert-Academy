# 먼저 움직이고 판단하기
def move(hive):
    for i, h in enumerate(hive):
        if h[3]==1:
            hive[i][0] -= 1
        elif h[3]==2:
            hive[i][0] += 1
        elif h[3]==3:
            hive[i][1] -= 1
        elif h[3]==4:
            hive[i][1] += 1

    return hive

# 끝처리와 만났을 때 처리하기
def status_check(hive, N):
    h_table = {}
    #점 별로 배열 모아두기
    for Hive in hive:
        if (Hive[0], Hive[1]) in h_table:
            h_table[Hive[0], Hive[1]].append(Hive)
        else:
            h_table[Hive[0], Hive[1]] = [Hive]
    #같은 점에 있는 것 하나로 합치기
    for H in h_table:
        if len(h_table[H]) > 1:
            h_table[H].sort(key = lambda x : x[2])
            num_MO = 0
            for h in h_table[H]:
                num_MO += h[2]
                hive.remove(h)
            hive.append([h[0], h[1], num_MO, h[3]])   
    #끝점에 도착했을 때 반으로 줄이고 방향 바꾸기
    num_MO = 0
    for i, Hive in enumerate(hive):
        if Hive[0]==0 or Hive[0]==N-1 or Hive[1]==0 or Hive[1]==N-1:
            hive[i][2] = int(hive[i][2]/2)
            if hive[i][3]==1:
                hive[i][3] = 2
            elif hive[i][3]==2:
                hive[i][3] = 1
            elif hive[i][3]==3:
                hive[i][3] = 4
            elif hive[i][3]==4:
                hive[i][3] = 3
        num_MO += Hive[2]
     
    return hive, num_MO
     
T = int(input())
 
for t in range(1, T+1):
    N, M, K = list(map(int, input().split()))

    hive = []
    for i in range(K):
        hive.append(list(map(int, input().split())))
 
    for _ in range(M):
        hive = move(hive)
        hive, num_MO = status_check(hive, N)

    print('#%s %s'%(t, num_MO))