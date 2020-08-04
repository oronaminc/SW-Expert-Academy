for _ in range(10):
    T = int(input())
    LIST = [list(map(int,input().split())) for i in range(T)]
    LIST, SUM = list(map(list, zip(*LIST))), 0
    for col_idx in range(T):
        temp = []
        for row_idx in range(T):
            if LIST[col_idx][row_idx] != 0: temp.append(LIST[col_idx][row_idx])
        if len(temp) == 1: temp = []
        for idx, item in enumerate(temp):
            if item == 1:
                temp = temp[idx:]
                break
        if len(temp) == 1: temp = []
        for idx in range(len(temp)-1, -1, -1):
            if temp[idx] == 2:
                temp = temp[:idx+1]
                break
        for idx,item in enumerate(temp):
            if item==2:
                if idx == len(temp)-1: SUM += 1
                elif temp[idx+1]==1: SUM += 1
    print("#{} {}".format(_+1, SUM))