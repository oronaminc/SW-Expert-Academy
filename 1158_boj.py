"""
def search(K):
    K+=1
    if K>N: K=1
    while(not arr2[K]):
        K += 1
        if K>N: K=1
        if(arr2.count(False)==N):
            return K
    return K

N,M = map(int,input().split())
arr=[j for j in range(N+1)]
arr2=[True]*(N+1)
arr3=[]
K=M
for i in range(N+1):
    if arr2[K]:
        arr3.extend([arr[K]])
        arr2[K]=False
        for j in range(M):
            K = search(K)
    else:
        K += 1
        if K>N: K=1
print("<"+", ".join(map(str,arr3))+">")
"""
N, M = map(int, input().split())
j = [str(i) for i in range(1, N+1)]
print(j)
m_len, cnt, res = N, 0, []

while j:
	cnt = (cnt+M-1) % m_len
	res.append(j.pop(cnt))
	m_len -= 1

print('<' + ', '.join(res) + '>')