import re

word = str(input())
result = re.findall("[a-zA-Z]+",word)
print(len(result))

"""
A = input().split()
print(len(A))
"""


"""
sum = 0
for x in A:
    if x == ' ':
        sum += 1
#if A[0] == " ":
#    sum -= 1
#if A[-1] == " ":
#    sum -=1

print(sum+1)    

"""