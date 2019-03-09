T = int(input())
 
for tc in range(T):
    N = int(input())
    bus_stops = [0]* 5001
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            bus_stops[j] += 1
    P = int(input())
    s = ''
    for i in range(P):
        s += f'{bus_stops[int(input())]} '
    print(f'#{tc+1} {s}')