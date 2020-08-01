# 라스트
## DFS 해줄 땐, 변수는 새로운 변수 이름으로 인자를 넘기고, 배열일 경우에는 다시 돌려 두거나 아니면 DEEPCOPY 하
def DFS(idx, answer):
    global MIN, MAX
    if idx == N-1:
        if MIN > answer: MIN = answer
        if MAX < answer: MAX = answer        
        return
    for i in range(4):
        if OPERATOR[i] > 0:
            OPERATOR[i] -= 1
            if i==0: new_answer = answer + NUM[idx+1]
            elif i==1: new_answer = answer - NUM[idx+1]
            elif i==2: new_answer = answer * NUM[idx+1]
            elif i==3: new_answer = int(answer/NUM[idx+1])
            DFS(idx+1, new_answer)
            OPERATOR[i] += 1
# T = int(input())
T = 1
for _ in range(T):
    # N = int(input())
    # OPERATOR = list(map(int, input().split()))
    # NUM = list(map(int, input().split()))
    N = 5
    OPERATOR = [2,1,0,1]
    NUM = [3,5,3,7,9]
    MIN, MAX = float('inf'), float('-inf')
    DFS(0, NUM[0])
    print(MAX-MIN)
'''
# 혼자 푼 코드
def DFS(OPERATOR, answer, NUM):
    global MIN, MAX
    if not NUM:
        if MIN > answer: MIN = answer
        if MAX < answer: MAX = answer
        return
    # 통으로 한 번에 보내줌, 시간과 공간 낭비가 심
    for idx in range(4):
        OPERATOR_COPY= [item for item in OPERATOR]
        NUM_COPY  = [item for item in NUM]
        temp_answer = answer
        if OPERATOR_COPY[idx] > 0:
            OPERATOR_COPY[idx] -= 1
            if idx == 0: temp_answer = temp_answer+NUM_COPY[0]
            if idx == 1: temp_answer = temp_answer-NUM_COPY[0]
            if idx == 2: temp_answer = temp_answer*NUM_COPY[0]
            if idx == 3: temp_answer = int(temp_answer/NUM_COPY[0])
            DFS(OPERATOR_COPY, temp_answer, NUM_COPY[1:])    
    
# T = int(input())
T = 1
for _ in range(T):
    # N = int(input())
    # OPERATOR = list(map(int, input().split()))
    # NUM = list(map(int, input().split()))
    N = 4
    OPERATOR = [2,1,0,1]
    NUM = [3,5,3,7,9]
    # OPERATOR =[0 ,2, 1, 0]
    # NUM = [1, 9, 8, 6]
    OPER, MIN, MAX = [], float('inf'), float('-inf')
    DFS(OPERATOR, NUM[0], NUM[1:])
    print(">>", MIN, MAX)


# 시간 초과
from itertools import permutations
# T = int(input())
T = 1
for _ in range(T):
    # N = int(input())
    # OPERATOR = list(map(int, input().split()))
    # NUM = list(map(int, input().split()))
    N = 4
    # OPERATOR = [2,1,0,1]
    # NUM = [3,5,3,7,9]
    OPERATOR =[0 ,2, 1, 0]
    NUM = [1, 9, 8, 6]
    OPER, MIN, MAX = [], float('inf'), float('-inf')
    for idx, val in enumerate(OPERATOR):
        for num in range(val): OPER.append(idx)
    print(">>", OPER)
    for item in permutations(OPER, len(OPER)):
        left_num = NUM[0]
        for oper, num in zip(item,NUM[1:]):
            if oper == 0: left_num += num
            elif oper == 1: left_num -= num
            elif oper == 2: left_num *= num
            elif oper == 3:
                if left_num < 0: left_num = -((-left_num)//num)
                else: left_num : left_num = left_num // num
        print(left_num)
        if left_num > MAX: MAX = left_num
        if left_num < MIN: MIN = left_num
        
    print(MIN, MAX)
        

from itertools import permutations
operator = [2,1,0,1]
num_list = [3,5,3,7,9]

operator = [2,1,6,2]
num_list = [2, 3, 7, 9, 4, 5, 1, 9,2, 5, 6, 4 ]
operator_num = [0]*operator[0]+[1]*operator[1]+[2]*operator[2]+[3]*operator[3]
temp_list = sorted(permutations(operator_num, len(operator_num)))
pre, done_list = temp_list[0], [temp_list[0]]
for item in temp_list:
    if item == pre:continue
    else:
        done_list.append(item)
        pre = item
print(done_list)
MAX, MIN = float('-inf'), float('inf')
for item in done_list:
    temp = num_list[0]
    for idx, op in enumerate(item):
        if op==0: temp = temp+num_list[idx+1]
        elif op==1: temp = temp-num_list[idx+1]
        elif op==2: temp = temp * num_list[idx+1]
        elif op==3: 
            if temp < 0: temp= -(abs(temp)//num_list[idx+1])
            else:temp = temp//num_list[idx+1]
    MIN = temp if temp < MIN else MIN
    MAX = temp if temp > MAX else MAX
    
print(MAX-MIN)    
    



def dfs(idx,result):
    global max_num
    global min_num
    if idx == N-1: # 연산은 주어진 숫자보다 1번 적으므로 N-1까지 탐색
        if max_num <= result:  max_num = result
        if result <= min_num:  min_num = result
        return
 
    for i in range(4): # 연산 4번 만큼 반복
        print(i, end=' ')
        if moderator[i] > 0: # 연산자가 존재한다면
            moderator[i] -= 1 # 해당 연산자를 한번 사용한다는 뜻
            if i == 0: new_result = result + number[idx+1]   
            elif i == 1: new_result = result - number[idx+1]
            elif i == 2: new_result = result * number[idx+1]
            else: # 나눗셈의 경우 음수 나눗셈 때문에 주의가 필요함. int형을 통해 버림을 취함
                new_result = int(result / number[idx+1])
            dfs(idx+1,new_result)
            moderator[i] += 1
 
T = int(input())
for t in range(T):
    N = int(input())
    moderator = list(map(int,input().split())) # [+ - * /]순으로 저장
    number = list(map(int,input().split()))
    max_num = -9999990
    min_num = 99999999
    dfs(0,number[0])
    print()
    print('#{} {}'.format(t+1,max_num-min_num))
'''