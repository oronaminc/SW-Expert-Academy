import itertools
# 지금 상태가 통과 되는 지 검사하는 부분
def check(chc):
    for x in range(W):
        cnt=0
        for y in range(D-1):
            if chc[y][x] == chc[y+1][x]:
                cnt += 1
                if cnt >= K-1:
                    break
            else:
                cnt = 0
        if cnt<K-1:
            return False
    return True
 
for _ in range(int(input())):
    D,W,K = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(D)]
    if check(arr):
        print(f"#{_+1} 0")
    else:
        arr2=[i for i in range(D)]
        for k in range(1,K+1):
            flag=0
            mycombination = itertools.combinations(arr2,k)
            for mycomb in mycombination:
                test=arr[:]
                for comb in mycomb:
                    test[comb]=[0 for j in range(W)]
                if check(test):
                    print(f"#{_+1} {k}")
                    flag=1
                    break
                else:
                    for comb in mycomb:
                        test[comb] = [1 for j in range(W)]
                    if check(test):
                        print(f"#{_+1} {k}")
                        flag=1
                        break
            if flag == 1:
                break
                
'''for comb in mycomb:
                    for comb2 in(0,1):
                        test[comb]=[comb2 for j in range(W)]
                        if check(test):
                            print(f"#{_+1} {k}")
                            flag=1
                            break
                            '''