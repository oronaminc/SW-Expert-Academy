#최종 code
def DFS(month, price):
    global MIN
    if price > MIN: return
    if month>=12:
        if MIN > price: MIN = price
        return
    DFS(month+1,PLAN[month]*PRICE[0]+price)
    DFS(month+1,PRICE[1]+price)
    DFS(month+3,PRICE[2]+price)


# T = int(input())
T = 1
for _ in range(T):
    # PRICE = list(map(int, input().split()))
    # PLAN = list(map(int, input().split()))
    PRICE = [10,40,100,300]
    PLAN = [0, 0, 2, 9, 1, 5, 0, 0, 0, 0, 0, 0]
    MIN = PRICE[-1]
    DFS(0,0)
    print(MIN)
"""
from itertools import combinations

# price = [10, 40, 100, 300]
# plan = [0, 0, 2, 9, 1, 5, 0, 0, 0, 0, 0, 0]

price = [10, 100, 50, 300]
plan = [0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 7, 8]

# price = [10, 100, 200, 1060]
# plan = [12, 9, 11, 13, 11, 8 ,6, 12, 8, 7 ,15, 6]

test1 = [3]*4
test2 = [3]*3+[1]*3
test3 = [3]*2+[1]*6
test4 = [3]*1+[1]*9
test5 = [1]*12
TEST = [set(range(len(test1))), set(range(len(test2))), set(range(len(test3))), set(range(len(test4))), set(range(len(test5)))]
year_price, answer, temp = price[-1], 0, [0]*12
for idx, p in enumerate(plan):
    if p: temp[idx] = min(plan[idx]*price[0], price[1])
MIN, cnt = float('inf'), 4
for test in TEST:
    for item in combinations(test, cnt):
        temp_list, start_idx, temp_val = [1]*len(test), 0, 0
        for idx in item: temp_list[idx] = 3
        for idx in temp_list:
            if idx == 1:
                temp_val += temp[start_idx]
                start_idx+=1
            if idx == 3:
                temp_val += price[2]
                start_idx+=3
        if MIN > temp_val: MIN = temp_val
    cnt -= 1
answer = year_price if year_price<MIN else MIN
print(answer)

def swim(idx,money):
    global min_price
    if idx >= 12: 
        if money < min_price: # 최소 비용 비교 
            min_price = money
        return
    if plan[idx]: # 운영 계획이 존재 할 때
        for i in range(4): # 비용을 기준으로 탐색하므로 비용의 개수인 4번만큼 반복
            if i == 0: # 1일권 
                swim(idx+1,money+price[i]*plan[idx])
            elif i == 1: # 1달권
                swim(idx+1,money+price[i])
            elif i == 2: # 3개월권
                swim(idx+3,money+price[i])
            else: # 1년권
                swim(idx+12,money + price[i])
    else: # 운영계획이 존재 안한다면 idx를 1만큼 늘려서 다시 탐색
        swim(idx+1,money)
 
T = int(input())
for t in range(T):
    price = list(map(int,input().split()))
    plan = list(map(int,input().split()))
    min_price = 99999999
 
    swim(0,0)
    print('#{} {}'.format(t+1,min_price))
"""