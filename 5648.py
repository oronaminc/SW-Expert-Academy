def vague_meet(atom, score):
    # x의 값이 같을 때, 점들을 모아봐요
    check_dic = {}  
    for Atom in atom:
        if Atom[0] in check_dic:
            check_dic[Atom[0]].append(Atom)
        else:
            check_dic[Atom[0]] = [Atom]
    # 서로 애매하게 만날 때 점수를 추가해요
    for c in check_dic:
        check_dic[c].sort()
        for i in range(len(check_dic[c])-1):
            if check_dic[c][i+1][1]-check_dic[c][i][1]==1 and check_dic[c][i][2]==0 and check_dic[c][i+1][2]==1:
                score += check_dic[c][i][3]
                score += check_dic[c][i+1][3]
                atom.remove(check_dic[c][i])
                atom.remove(check_dic[c][i+1])
 
    # y 값이 같을 때, 점들을 모아봐요
    check_dic = {}  
    for Atom in atom:
        if Atom[1] in check_dic:
            check_dic[Atom[1]].append(Atom)
        else:
            check_dic[Atom[1]] = [Atom]
    # 서로 애매하게 만날 때 점수를 추가해요
    for c in check_dic:
        check_dic[c].sort()
        for i in range(len(check_dic[c])-1):
            if check_dic[c][i+1][0]-check_dic[c][i][0]==1 and check_dic[c][i][2]==3 and check_dic[c][i+1][2]==2:
                score += check_dic[c][i][3]
                score += check_dic[c][i+1][3]
                atom.remove(check_dic[c][i])
                atom.remove(check_dic[c][i+1])
 
    return atom, score
 
def fit_meet(atom, score):
    del_list = []
    for Atom in atom:
        if Atom[2]==0:
            Atom[1] += 1
            if Atom[1] > 1000:
                del_list.append(Atom)
 
        elif Atom[2]==1:
            Atom[1] -= 1
            if Atom[1] < -1000:
                del_list.append(Atom)
 
        elif Atom[2]==2:
            Atom[0] -= 1
            if Atom[0] < -1000:
                del_list.append(Atom)
 
        else:
            Atom[0] += 1
            if Atom[0] > 1000:
                del_list.append(Atom)
 
    for d in del_list:
        atom.remove(d)
 
 
    check_dic = {}
    for Atom in atom:
        if (Atom[0], Atom[1]) in check_dic:
            check_dic[Atom[0], Atom[1]].append(Atom)
        else:
            check_dic[Atom[0], Atom[1]] = [Atom]
 
    for c in check_dic:
        if len(check_dic[c]) > 1:
            for i in range(len(check_dic[c])):
                score += check_dic[c][i][3]
                atom.remove(check_dic[c][i])
     
    return atom, score
 
 
T = int(input())
for t in range(1,T+1):

    N = int(input())
    atom = [list(map(int, input().split())) for i in range(N)]
 
    score = 0
    for _ in range(2000):
        atom, score = vague_meet(atom, score)
        atmo, score = fit_meet(atom, score)
 
    print(f'#{t} {score}')