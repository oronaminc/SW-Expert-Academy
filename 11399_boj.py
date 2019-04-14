T=int(input())
arr=list(map(int,input().split()))
arr.sort()
sum = 0
for i in arr:
    sum += T*i
    T -= 1
print(sum)