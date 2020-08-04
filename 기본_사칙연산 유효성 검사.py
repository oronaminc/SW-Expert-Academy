def inorder(tree, index):
    root = tree[index]
    if len(root) == 1: return int(root[0])
    left = inorder(tree, int(root[1]) - 1)
    operator = root[0]
    right = inorder(tree, int(root[2]) - 1)
    if operator == '+': return left + right
    elif operator == '-':  return left - right
    elif operator == '*':  return left * right
    elif operator == '/':
        if right == 0: right = 1
        return left / right


for _ in range(10):
    N = int(input())
    tree, ans = [], 1
    for i in range(N): tree.append(list(input().split())[1:])
    try: int(inorder(tree, 0))
    except: ans = 0
    print("#{} {}".format(_ + 1,ans))