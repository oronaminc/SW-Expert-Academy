from sys import stdin

arr = list(map(int,stdin.readline().split()))
arr_s = set(arr)
arr2=[]
ans = ""
#A=[False]*(2**25)
for i in range(len(arr)):
    if arr.count(arr[i]) > 1:
        arr2.extend([(arr[i],i)]) 
    else: continue
arr_s=set()
arr3=[]
for i in arr2:
    if i[0] in arr_s: arr3.extend([i[1]])
    else: arr_s.add(i[0])
arr3.reverse()
for i in arr3: arr.pop(i)
for i in arr: print(i,end=" ")
    #if A[arr[i]]:
    #    continue
    #else:
    #   ans = ans + str(arr[i]) +" "
    #    #arr2.extend([arr[i]])
    #    A[arr[i]] = True

#arr2.sort(reverse=True)
#arr2.reverse()
#print(arr2)


#temp=[]
#for i in range(len(arr2)):
#    if i%2 == 0:
#        temp.extend([])

#result = sorted(temp, key=lambda i:i[0], reverse=True)
#print(result)
#arr2.sort(reverse=True, key=lambda j:j[0])
#print(arr2)
#for i in arr2:
#    print(i)

'''

import sys
import os
n = 2**22
a = bytearray(n)
m = 8
unstdin = os.fdopen(sys.stdin.fileno(), 'rb', 1000000)
while True:
    try:
        b = 0
        while True:
            ch = unstdin.read(1)
            if b'0' <= ch <= b'9':
                b = 10*b+int(ch)
            elif ch == b' ':
                break
            else:
                raise EOFError
    except EOFError:
        break
    x, y = b % m, b // m
    if not a[y] & (1<<x):
        print(b, end = ' ')
    a[y] |= (1<<x)
if b:
    x, y = b % m, b // m
    if not a[y] & (1<<x):
        print(b, end = '')
        '''