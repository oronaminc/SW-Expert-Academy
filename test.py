import itertools

arr = list(map(int, input().split()))
arr.sort(reverse=True)
print(arr)

for _ in itertools.combinations(arr,3):
    if(_[0] < _[1]+_[2]):
        print(_)
    
    

a = ['a', 'b', 'c', 'd']
a.insert(0,a.pop()) #시계방향
#print(a)
b = ['a', 'b', 'c', 'd']
b.append(b.pop(0)) #반시계 방향
#print(b)
b = ('a', 'b', 'c', 'd')

list_enum = list(enumerate(a))
tuple_enum = tuple(enumerate(b))

#print(list_enum)
#print(tuple_enum)
#print(tuple_enum[0][1])
candi=[i for i in range(6)]
#print(candi)

"""
import re
text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
regex = re.compile("에러 1033")
mo = regex.search(text)
if mo != None:
    print(mo.group()) 
    """