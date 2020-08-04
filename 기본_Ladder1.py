for _ in range(10):
    T = int(input())
    LIST = [list(map(int,input().split())) for i in range(100)]
    IDX = [idx for idx, x in enumerate(LIST[0]) if x==1]
    for start_idx in IDX:
        row_idx = start_idx
        for col_idx in range(100):
            if row_idx-1>-1 and LIST[col_idx][row_idx-1] == 1:
                while row_idx > -1 and LIST[col_idx][row_idx] == 1: row_idx -= 1
                row_idx += 1
            elif row_idx+1<100 and LIST[col_idx][row_idx+1] == 1:
                while row_idx < 100 and LIST[col_idx][row_idx] == 1: row_idx += 1
                row_idx -= 1
            else: continue
        if LIST[col_idx][row_idx] == 2: break
    print("#{} {}".format(T,start_idx))