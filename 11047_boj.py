N, K = map(int,input().split())
arr=[int(input()) for i in range(N)]
arr.sort(reverse=True)
sum = 0
for i in arr:
    sum += (K//i)
    K = K%i
print(sum)