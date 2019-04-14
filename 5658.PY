T = int(input())
for _ in range(T):
    N, K = map(int,input().split())
    pw = list(input())
    pw_set=set()
    n = N//4
    for k in range(n):
        for i in range(4):
            tmp =""
            for j in range(n):
                tmp += pw[i*n + j]
            pw_set.add(tmp)
        pw.append(pw.pop(0))
    result = []
    for X in pw_set:
        result.append(int(X,16))
    result.sort(reverse=True)
    print(f'{_+1} {result[K-1]}')    
