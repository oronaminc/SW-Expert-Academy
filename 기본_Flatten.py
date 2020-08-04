for _ in range(10):
    CNT = int(input())
    LIST = list(map(int,input().split()))
    LIST.sort()
    for cnt in range(CNT):
        LIST[0]+=1
        LIST[-1] -=1
        LIST.sort()
    print("#{} {}".format(_+1, LIST[-1]-LIST[0]))