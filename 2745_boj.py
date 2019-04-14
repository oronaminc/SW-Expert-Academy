def ch_chr(c):
    if c>='A' : return ord(c)-55
    else: return int(c)

N, B = input().split()
B = int(B)
n = len(N)-1
sum = 0

for i in N:
    sum += ch_chr(i)*(B**n)
    n -= 1

print(sum)