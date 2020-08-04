for _ in range(10):
    N, START = map(int,input().split())
    LIST = list(map(int,input().split()))
    DICT, SET, BST, TEMP = {}, set(), [], []
    for idx in range(len(LIST)-1):
        if idx%2==0:
            SET.update([LIST[idx], LIST[idx+1]])
            DICT[LIST[idx]] = DICT.get(LIST[idx], []) + [LIST[idx+1]]
    BST.append([START, 0])
    TEMP.append([START, 0])
    while BST:
        item, idx = BST.pop(0)
        if item in SET:
            SET.remove(item)
            if item in DICT.keys():
                for new_item in DICT[item]:
                    if new_item in SET:
                        BST.append([new_item, idx+1])
                        TEMP.append([new_item, idx+1])
    TEMP = sorted(TEMP, key=lambda x:x[0], reverse= True)
    TEMP = sorted(TEMP, key=lambda x:x[1], reverse= True)
    print("#{} {}".format(_+1, TEMP[0][0]))