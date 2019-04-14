from sys import stdin
input = stdin.readline
N = int(input())
arr=[int(input()) for i in range(N)]
rank=[j for j in range(1,N+1)]
arr.sort(reverse=True)
maxx = -1
sum = 0
k=0
for i in arr:
    if i+N >= maxx:
        if i+(k+1) > maxx: maxx = i+(k+1)
        sum += 1
    k+=1
print(sum)