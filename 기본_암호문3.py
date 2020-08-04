for _ in range(10):
    T = int(input())
    LIST = list(input().split())
    N = int(input())
    CMD = list(input().split())
    for idx, item in enumerate(CMD):
        if item == 'I': LIST = LIST[:int(CMD[idx+1])] + CMD[idx+3:idx+3+int(CMD[idx+2])] + LIST[int(CMD[idx+1]):]
        elif item == 'D': LIST = LIST[:int(CMD[idx+1])] + LIST[int(CMD[idx+1])+int(CMD[idx+2]):]
        elif item == 'A': LIST = LIST+CMD[idx+2:idx+2+int(CMD[idx+1])]
    print("#{} {}".format(_+1, ' '.join(LIST[:10])))