from sys import stdin

A = list(map(int,stdin.readline().split()))
B = list(map(int,stdin.readline().split()))
num_a = 0;arr_a = 0;num_b = 0;arr_b = 0;k=-1
for i in range(10):
    if A[i] > B[i]:
        num_a += 3
    elif A[i] < B[i]:
        num_b += 3
    else:
        num_a+=1
        num_b+=1
    if A[i]!=B[i]:
        k=i
print(num_a,num_b)
cha = ""
if num_a > num_b: cha="A"
elif num_a < num_b: cha="B"
elif k<0: cha="D"
elif A[k]>B[k]: cha="A"
else: cha="B"
print(cha)