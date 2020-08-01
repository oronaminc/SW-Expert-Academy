#라스
# T = int(input())
T = 1
for _ in range(T):
    # N,M,K,A,B = map(int,input().split())
    N,M,K,A,B = 2,2,6,1,2
    # A_TIME = list(map(int,input().split()))
    # B_TIME = list(map(int,input().split()))
    # TIME = list(map(int,input().split()))
    A_TIME = [3,2]
    B_TIME = [4,2]
    TIME = [0,0,1,2,3,4]
    TIME = [[idx+1,item] for idx,item in enumerate(TIME)]
    print(TIME)
    A_LIST = [[] for i in range(N)]
    B_LIST = [[] for i in range(M)]
    time, queue_first, queue_second, CNT, L, A_SET, B_SET = 0, [], [], 0, len(TIME), set(), set()
    while CNT < L:
        while TIME:
            if TIME[0][1] <= time: queue_first.append(TIME.pop(0)[0])
            else: break
        # print(queue_first, TIME)
        temp_queue_second = []
        for idx, item in enumerate(A_LIST):
            if item:
                A_LIST[idx][1] -= 1
                if A_LIST[idx][1] == 0:
                    temp_queue_second.append([A_LIST[idx][0], idx])
                    A_LIST[idx] = []
            if not A_LIST[idx] and queue_first:
                A_LIST[idx] = [queue_first.pop(0), A_TIME[idx]]
                if idx+1 == A: A_SET.add(A_LIST[idx][0])
        
        queue_second += sorted(temp_queue_second, key=lambda x: x[1])
        for idx, item in enumerate(B_LIST):
            if item:
                B_LIST[idx][1] -=1
                if B_LIST[idx][1] == 0:
                    B_LIST[idx] = []
                    CNT += 1
            if not B_LIST[idx] and queue_second:
                B_LIST[idx] = [queue_second.pop(0)[0], B_TIME[idx]]
                if idx+1 == B: B_SET.add(B_LIST[idx][0])
        
        print(time, A_LIST, B_LIST)
        print()
        time += 1
    answer = -1 if not (A_SET&B_SET) else sum(A_SET&B_SET)
    print(answer)
        

"""
from heapq import *
# T = int(input())
T = 1
for _ in range(T):
    # N,M,K,A,B = map(int, input().split())
    # N,M,K,A,B = 2,2,6,1,2
    N,M,K,A,B = 3,2,10,1,2
    # RECEPT = list(map(int, input().split()))
    # REPAIR = list(map(int, input().split()))
    # delay = list(map(int, input().split()))
    # RECEPT = [3,2]
    # REPAIR = [4,2]
    RECEPT = [5,5,8]
    REPAIR = [3,5]

    # delay = [0,0,1,2,3,4]
    delay = [0,0,4,7,8,8,9,9,10,10]

    RECEPT_L = [[] for i in range(N)]
    REPAIR_L = [[] for i in range(M)]
    recept_wait, repair_wait = [], []
    time = 0
    A_SET, B_SET = set(), set()
    total = 0
    
    while total < K:
        print("time : ",time, total, K)
        for idx, delay_time in enumerate(delay):
            if delay_time == time: recept_wait.append(idx)
        temp_repair_wait = []
        for idx, recept in enumerate(RECEPT_L):
            if not recept and recept_wait:
                RECEPT_L[idx] = [recept_wait.pop(0),RECEPT[idx]]
                if idx+1 == A: A_SET.add(RECEPT_L[idx][0]+1)
            elif recept:
                RECEPT_L[idx][1]-=1
                if RECEPT_L[idx][1] == 0:
                    repair_wait.append(RECEPT_L[idx][0])
                    if recept_wait:
                        RECEPT_L[idx] = [recept_wait.pop(0),RECEPT[idx]]
                        if idx+1 == A: A_SET.add(RECEPT_L[idx][0]+1)
                    else: RECEPT_L[idx] = []
        for idx, repair in enumerate(REPAIR_L):
            if not repair and repair_wait:
                REPAIR_L[idx] = [repair_wait.pop(0),REPAIR[idx]]
                if idx+1 == B: B_SET.add(REPAIR_L[idx][0]+1)
            elif repair:
                REPAIR_L[idx][1]-=1
                if REPAIR_L[idx][1]==0:
                    if repair_wait:
                        REPAIR_L[idx] = [repair_wait.pop(0),REPAIR[idx]]
                        if idx+1 == B: B_SET.add(REPAIR_L[idx][0]+1)
                    else: REPAIR_L[idx] = []
                    total += 1
        print('recept_wait', recept_wait)
        print('repair_wait', repair_wait)
        print("RECEPT_L : ", RECEPT_L)
        print("REPAIR_L : ", REPAIR_L)
        print()
        time += 1
    answer = -1 if sum(A_SET & B_SET) == 0 else sum(A_SET & B_SET) 
    print(A_SET, B_SET, answer)
"""