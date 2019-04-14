K=int(input())
N=int(input())
arr=[list(input().split()) for i in range(N)]
time=0
pos=K
for q in arr:
    if time+int(q[0]) >= 210:
        break
    if q[1] == 'T':
        pos = 1 if pos==8 else pos+1
    time += int(q[0])
print(pos)