import itertools
T = int(input())
for _ in range(T):
    ans = 999999
    N = int(input())
    arr = [list(map(int,input().split())) for i in range(N)]
    num=[n for n in range(N)]
    COMB = itertools.combinations(num,len(num)//2)
    for combi in COMB:
        rev = set(set(num)-set(combi))
        A,B=0,0
        for comb in combi:
            for comb2 in combi:
                if comb != comb2: A += arr[comb][comb2]
        for rev1 in rev:
            for rev2 in rev:
                if rev1 != rev2: B += arr[rev1][rev2]
        if abs(A-B) < ans:
            ans = abs(A-B)
    print(f'#{_+1} {ans}')