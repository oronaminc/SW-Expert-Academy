for _ in range(10):
    T, N = map(int,input().split())
    LIST = list(map(int,input().split()))
    DICT = dict()
    for idx in range(len(LIST)//2):
        IDX, ITEM = LIST[idx*2], LIST[idx*2+1]
        DICT[IDX] = DICT.get(IDX, []) +[ITEM]
    item_set, QUEUE, FLAG = set(DICT.keys())-{0}, DICT[0], False
    while QUEUE:
        item = QUEUE[0]
        if item in item_set:
            for add_item in DICT[item]:
                if add_item == 99:
                        FLAG = True
                        break
                if add_item in item_set: QUEUE.append(add_item)
            if FLAG: break
            item_set.remove(item)
        QUEUE.pop(0)
    print("#{} {}".format(_+1,int(FLAG)))