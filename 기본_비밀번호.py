for _ in range(10):
    N, NUM_LIST = input().split()
    NUM_LIST, flag = [int(x) for x in NUM_LIST], True
    while flag:
        flag = False
        for idx in range(len(NUM_LIST)-1):
            if NUM_LIST[idx] == NUM_LIST[idx+1]:
                del NUM_LIST[idx]
                del NUM_LIST[idx]
                flag = True
                break
    print("#{} {}".format(_+1,''.join(str(x) for x in NUM_LIST)))