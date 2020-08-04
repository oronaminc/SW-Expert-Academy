def square(N,M,SUM):
    global ans
    if M==1:
        ans = SUM
        return
    square(N, M-1, SUM*N)

for _ in range(10):
    T = int(input())
    N,M = map(int,input().split())
    ans = 0
    square(N,M,N)
    print("#{} {}".format(T,ans))