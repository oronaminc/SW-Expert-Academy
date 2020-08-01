"""
T = int(input())
for _ in range(1, T+1):
    N, K = map(int, input().split())
    pw_set = set()
    pw = list(input())
    num = N//4
    for k in range(num):
        for i in range(4):
            temp = ''
            for j in range(num):
                temp += pw[i*num + j]
            pw_set.add(temp)
        pw.append(pw.pop(0))
    result = []
    for X in pw_set:
        result.append(int(X, 16))
    result.sort(reverse=True)
    print(f'#{_} {result[K-1]}')
"""


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    treasure = input()
    num_set = set()
    for __ in range(N//3):
        for num in range(4):
            start_idx = N//4 * num
            num_set.add(int(treasure[start_idx:start_idx+N//4],16))
        treasure = treasure[1:]+treasure[0]
    num_list = sorted(num_set, reverse=True)
    print("#{} {}".format(_+1,num_list[K-1])) 