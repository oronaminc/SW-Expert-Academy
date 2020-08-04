def inorder(NODE):
    if NODE == False: return
    inorder(DICT[NODE][0])
    print(CHR[NODE-1], end="")
    inorder(DICT[NODE][1])
    
for _ in range(10):
    DICT = {} 
    N = int(input())
    NODE, CHR = [list(input().split()) for i in range(N)], []
    for item in NODE: CHR.append(item[1])
    for item in NODE:
        if len(item) == 4: DICT[int(item[0])] = [int(item[2]), int(item[3])]
        elif len(item) == 3: DICT[int(item[0])] = [int(item[2]), False]
        else: DICT[int(item[0])] = [False, False]
    print("#{} ".format(_+1), end='')
    inorder(1)
    print()
    
        
    