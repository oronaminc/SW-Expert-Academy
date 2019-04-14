'''
import re
from sys import stdin
data="""
park 800905-1049118
kim 700905-1059119
"""
T = int(input())
for i in range(T):
    word = input()
    pat = re.compile("(\d{6})[-](\d{7})")
    print(pat.sub("\g<1>-*******", word))
'''

from itertools import permutations, product

#per = permutations(['빨','주','노','초'],3)
per = product(['3','6','9'], repeat=3)
print(list(per))
#pat = re.compile("(\d{6})[-]\d{7}")
#print(pat)
#print(pat.sub("\g<1>-*******", data))


