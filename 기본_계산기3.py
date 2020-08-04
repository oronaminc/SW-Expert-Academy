import re

def cal(NUM):
    NUM_list = re.split('\*|\+',NUM)
    stack, prior_idx = [int(NUM_list.pop(0))], -1
    for idx, item in enumerate(NUM):
        if item == '*': stack[-1] = int(stack[-1])*int(NUM_list.pop(0))
        elif item == '+': stack.append(int(NUM_list.pop(0)))
    return sum(stack)

for _ in range(10):
    input();num=input()
    num_copy,start_idx = num, -1
    while True:  
        for idx,item in enumerate(num):
            if item == "(": start_idx = idx
            elif item == ")":
                num_copy = num[:start_idx]+str(cal(num[start_idx+1:idx]))+num[idx+1:]        
                break
        if start_idx == -1: break
        num, start_idx = num_copy, -1
    print("#{} {}".format(_+1,num_copy))