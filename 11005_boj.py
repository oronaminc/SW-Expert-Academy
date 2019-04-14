N, B = map(int,input().split())

ans=""
while(N):
    left = N%B
    if(left >9):
        left = chr(left+55)
    ans = str(left)+ans
    N //= B
print(ans)