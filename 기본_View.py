for i in range(10):
    SUM = 0
    N=int(input())
    LIST = list(map(int,input().split()))
    for idx in range(2, len(LIST)-2):
        item = LIST[idx]
        if item > LIST[idx-1] and item > LIST[idx-2] and item > LIST[idx+1] and item > LIST[idx+2]:
            SUM += (item-max(LIST[idx-1],LIST[idx-2],LIST[idx+1],LIST[idx+2]))
    print("#{} {}".format(i+1,SUM))
        
                