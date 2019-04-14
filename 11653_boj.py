import math

N = int(input())
n = int(math.sqrt(N))
for i in range(2,n+1):
    while(N%i == 0):
        print(i)
        N //= i
if(N != 1):print(N)        