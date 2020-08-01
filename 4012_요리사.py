#최
from itertools import combinations
# T = int(input())
T = 1
for _ in range(T):
    # N = int(input())
    N = 4
    # FOOD = [list(map(int, input().split())) for i in range(N)]\
    FOOD = [[0, 5, 3, 8], [4, 0, 4, 1], [2, 5, 0, 3], [7, 2, 3, 0]]
    total_set, MIN = set(range(N)), float("inf")
    for item in combinations(total_set, N//2):
        right_sum, left_sum = 0, 0
        other_item = total_set - set(item)
        for x in set(item):
            for y in set(item):
                if x != y: right_sum += FOOD[x][y]
        for x in other_item:
            for y in other_item:
                if x!=y: left_sum += FOOD[x][y]
        if abs(left_sum-right_sum) < MIN: MIN = abs(left_sum-right_sum)
    print(MIN)
    
"""
from itertools import combinations

N = 4
food = [[0, 5, 3, 8], [4, 0, 4, 1], [2, 5, 0, 3], [7, 2, 3, 0]]
food_idx = set(range(N))
food_combi_list = list(map(set,(combinations(food_idx, N//2))))
MIN = float('inf')
for item in food_combi_list:
    left_food, left_sum = item, 0
    right_food, right_sum = food_idx-item, 0
    
    # for x,y in combinations(left_food,2): left_sum += (food[x][y]+food[y][x])
    # for x,y in combinations(right_food,2): right_sum += (food[x][y]+food[y][x])
    for x in left_food:
        for y in left_food:
            if x != y: left_sum += (food[x][y])
            
    for x in right_food:
        for y in right_food:
            if x != y: right_sum += (food[x][y])
    
    if MIN > abs(left_sum-right_sum): MIN = abs(left_sum-right_sum)
    
print("{}".format(MIN))
"""