num = int(input())
for i in range(num):
    a,b = map(int, input().split())
    list1 = [0] * (a+1)
    for j in range(1, b+1):
        c, d = map(int, input().split())
        for k in range(c, d+1):
            list1[k] = j

    output=""
    for ii in range(1,a+1):
        output += " "+str(list1[ii])

    print("#"+str(i+1)+output)