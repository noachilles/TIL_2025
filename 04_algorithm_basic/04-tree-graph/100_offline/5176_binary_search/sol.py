def inorder(idx):
    global value
    if idx <= N:
        inorder(idx * 2)
        tree[idx] = value
        value += 1
        inorder(idx * 2 + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    value = 1
    inorder(1)
    print(f'#{tc}', end=' ')
    print(tree[1], tree[N // 2])