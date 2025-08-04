import sys
sys.stdin = open('input.txt')

# 완전 이진 트리: 1~n까지 빈 노드 X
# 노드는 아래 그림과 같은 순서로 주어짐

def preorder(idx):
    # 입력된 index에 대해
    if idx <= N:
        # 왼쪽 자식 노드를 먼저 방문
        preorder(idx * 2)
        # 부모 노드를 방문
        res.append(tree[idx])
        # 오른쪽 자식 노드를 방문
        preorder(idx * 2 + 1)

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [''] * (N+1)
    for _ in range(N):
        # 입력 값들에 대해
        input_data = input().split()
        # 첫 번째, 두 번째 값만 저장 및 활용
        index, value = input_data[0:2]
        tree[int(index)] = value
    res = []
    # root Node의 index를 인자로 함수 호출
    preorder(1)
    print(f'#{tc}', end=' ')
    print(''.join(res))

# 일반항 구하기 ... ?
# 데이터를 불러오는 방법을 여러가지로 시도해보면 좋을듯