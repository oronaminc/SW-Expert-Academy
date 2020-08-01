from itertools import combinations
T = 1
# T = int(input())
for _ in range(T):
    # N = int(input())
    N = 5
    # MAP = [list(map(int,input().split())) for i in range(N)]
    MAP = [[0, 1, 1, 0, 0], [0, 0, 1, 0, 3], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [1, 0, 5, 0, 0]]
    # MAP = [[0, 0, 1, 1, 0], [0, 0, 1, 0, 2], [0, 0, 0, 1, 0], [0, 1, 0, 0, 0], [1, 0, 5, 0, 0]]
    PEOPLE, STAIR, MIN = [], [], float('inf')
    for col in range(N):
        for row in range(N):
            if MAP[col][row] == 1:PEOPLE.append([col,row])
            elif MAP[col][row] > 1:STAIR.append([col, row, MAP[col][row]])
    total_set = set(range(len(PEOPLE)))
    for cnt in range(len(PEOPLE)+1):
        for item in list(combinations(total_set, cnt)):
            A_SET, B_SET = set(item), total_set-set(item)
            A_LIST, B_LIST = [], []
            for idx in A_SET: A_LIST.append(abs(PEOPLE[idx][0]-STAIR[0][0])+abs(PEOPLE[idx][1]-STAIR[0][1]))
            for idx in B_SET: B_LIST.append(abs(PEOPLE[idx][0]-STAIR[1][0])+abs(PEOPLE[idx][1]-STAIR[1][1]))
            A_WAIT, B_WAIT,time,A_STAIR,B_STAIR, people_cnt = 0, 0, 0, [], [], 0       
            while people_cnt<len(PEOPLE):
                NEW_A_LIST, NEW_B_LIST = [], []
                if A_LIST:
                    for idx, a in enumerate(A_LIST):
                        if a == 0: A_WAIT += 1
                        else: NEW_A_LIST.append(A_LIST[idx]-1)
                    A_LIST = NEW_A_LIST
                if B_LIST:
                    for idx, b in enumerate(B_LIST):
                        if b == 0: B_WAIT += 1
                        else: NEW_B_LIST.append(B_LIST[idx]-1)
                    B_LIST = NEW_B_LIST        
                NEW_A_STAIR, NEW_B_STAIR = [], []
                for idx,a in enumerate(A_STAIR):
                    if a == 1: people_cnt += 1
                    if a > 1: NEW_A_STAIR.append(a-1)
                A_STAIR = NEW_A_STAIR
                for idx,b in enumerate(B_STAIR):
                    if b == 1: people_cnt += 1
                    if b > 1: NEW_B_STAIR.append(b-1)
                B_STAIR = NEW_B_STAIR
                for cnt in range(3):
                    if A_WAIT > 0 and len(A_STAIR) <3:
                        A_STAIR.append(STAIR[0][2])
                        A_WAIT -= 1
                for cnt in range(3):
                    if B_WAIT > 0 and len(B_STAIR) <3:
                        B_STAIR.append(STAIR[1][2])
                        B_WAIT -= 1
                
                time += 1
            if MIN > time: MIN = time
    print(MIN)
        
'''
from itertools import combinations
# T = int(input())
T = 1
for _ in range(T):
    # N = int(input())
    # MAP = [list(map(int, input().split())) for i in range(N)]
    N = 9
    # MAP = [[0, 1, 1, 0, 0], [0, 0, 1, 0, 3], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [1, 0, 5, 0, 0]]
    # MAP = [[0, 0, 1, 1, 0], [0, 0, 1, 0, 2], [0, 0, 0, 1, 0], [0, 1, 0, 0, 0], [1, 0, 5, 0, 0]]
    MAP = [[0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 8], [7, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0,
0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    PEOPLE, STAIR = [], []
    for col in range(N):
        for row in range(N):
            if MAP[col][row] == 1: PEOPLE.append([col,row])
            elif MAP[col][row] > 1: STAIR.append([col, row, MAP[col][row]])
    
    A_STAIR, B_STAIR = STAIR[0], STAIR[1]
    A_VAL, B_VAL = A_STAIR[2], B_STAIR[2]
    # print(A_VAL, B_VAL)
    MIN = float('inf')
    
    people_set = set(range(len(PEOPLE)))
    for i in range(len(PEOPLE)+1):
        for item in list(combinations(people_set, i)):
            A_PEOPLE, B_PEOPLE, =  [], []
            item = set(item)
            A_SET, B_SET = item, people_set-item
            AA_SET, BB_SET = A_SET.copy(), B_SET.copy()
            
            for person in A_SET: A_PEOPLE.append([person, abs(PEOPLE[person][0]-A_STAIR[0])+abs(PEOPLE[person][1]-A_STAIR[1])])
            for person in B_SET: B_PEOPLE.append([person, abs(PEOPLE[person][0]-B_STAIR[0])+abs(PEOPLE[person][1]-B_STAIR[1])])
            
    
            time, count = 0, 0
            stair_a, stair_b = [], []
            while count < len(people_set):
                time += 1
                for idx, item in enumerate(A_PEOPLE):
                    person, distance = item
                    distance -= 1
                    if distance <= -1 and person in A_SET and len(stair_a) < 3:
                        stair_a.append(A_VAL)
                        A_SET.remove(person)
                    A_PEOPLE[idx] = [person, distance]
                for idx, item in enumerate(B_PEOPLE):
                    person, distance = item
                    distance -= 1
                    if distance <= -1 and person in B_SET and len(stair_b) < 3:
                        stair_b.append(B_VAL)
                        B_SET.remove(person)
                    B_PEOPLE[idx] = [person, distance]
                done_stair_a, done_stair_b = [], []
                idx_a, idx_b = 0, 0
                for idx, item in enumerate(stair_a):
                    if item <= 0:
                        done_stair_a.append(idx)
                        count += 1
                    else: stair_a[idx] = item -1
                for idx, item in enumerate(stair_b):
                    if item <= 0:
                        done_stair_b.append(idx)
                        count += 1
                    else: stair_b[idx] = item -1
                for idx in done_stair_a[::-1]:  stair_a.pop(idx)
                for idx in done_stair_b[::-1]:  stair_b.pop(idx)
                # print(A_SET, B_SET)
                for item in A_PEOPLE:
                    if item[0] in A_SET and item[1] <= -1 and len(stair_a)<3:
                        stair_a.append(A_VAL-1)
                        A_SET.remove(item[0])
                for item in B_PEOPLE:
                    if item[0] in B_SET and item[1] <= -1 and len(stair_b)<3:
                        stair_b.append(B_VAL-1)
                        B_SET.remove(item[0])
                
                # print(time,A_PEOPLE,B_PEOPLE, "|", stair_a, stair_b, count)
                # print()
            if time < MIN :
                # print(AA_SET, BB_SET )
                MIN = time  

    print(MIN)
    '''