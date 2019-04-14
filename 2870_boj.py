"""
N = int(input())
arr = [input() for i in range(N)]
print(arr)
num = []
for word in arr:
    ch_num=""
    for ch in word:
        if ch>= 'a' and ch <= 'z':
            ch_num += " "
        else:
            ch_num += ch
    num.extend(map(int,ch_num.split()))    
num.sort()

for N in num:
    print(N)

"""
"""
import re
N = int(input()); paper=[]; res=str()
for i in range(N):
    for j in list(re.split("\\D", str(input()))):
        if j!="":paper.append(int(j))
paper.sort()
for i in paper: print(i)

"""
import re
N = int(input()); paper=[]; res=str()
for i in range(N):
    for j in list(re.split("\\D", str(input()))):
        print(j)
        if j!="":
            #print(j)
            paper.append(int(j))
paper.sort()
for i in paper:print(i)

"""
import re
a = input()

#m = p.match(a)
#m = p.search(a)

#p = re.compile('[a-z]+')
#m = p.findall(a)

#이것을 한 줄로 줄일 수 있는 데 바로
m = re.findall('\\D', a)

if m:
    #print('Match found: ', m.group())
    print(m)
else:
    print('No Match')

"""