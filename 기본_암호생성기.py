for _ in range(10):
    T = int(input())
    LIST = list(map(int,input().split()))
    num = 1
    while True:
        if num == 6: num = 1 
        temp_num = LIST.pop(0)-num
        LIST.append(temp_num)
        if temp_num<=0:
            LIST[-1] = 0
            break
        num += 1
    print("#{} {}".format(T,' '.join(str(x) for x in LIST)))