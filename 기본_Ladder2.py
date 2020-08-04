for _ in range(10):
    T = int(input())
    LIST = [list(map(int,input().split())) for i in range(100)]
    IDX = [idx for idx, x in enumerate(LIST[0]) if x==1]
    START, SUM_MIN = [], float('inf')
    for start_idx in IDX:
        row_idx, SUM = start_idx, 0
        for col_idx in range(100):
            if row_idx-1>-1 and LIST[col_idx][row_idx-1] == 1:
                while row_idx > -1 and LIST[col_idx][row_idx] == 1:
                    row_idx, SUM = row_idx-1, SUM+1
                row_idx, SUM = row_idx+1, SUM-1
            elif row_idx+1<100 and LIST[col_idx][row_idx+1] == 1:
                while row_idx < 100 and LIST[col_idx][row_idx] == 1:
                    row_idx, SUM = row_idx+1, SUM+1
                row_idx, SUM = row_idx-1, SUM-1
            else: continue
        if SUM < SUM_MIN: SUM_MIN, START = SUM, [start_idx]
        elif SUM == SUM_MIN: START.append(start_idx)
    print("#{} {}".format(T,max(START)))