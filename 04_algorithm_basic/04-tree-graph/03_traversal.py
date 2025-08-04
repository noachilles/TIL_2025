# 완전 이진 트리 기준 순회

# 전위 순회
def preorder_traversal(idx):
    # 어디까지 순회해야 하나?
    # 순회 대상이 범위 넘어가지 않도록
    if idx <= N:
        # 전위 순회는 부모 노드를 먼저 조사한다.
        print(tree[idx], end=' ')
        # left subtree에 대해서도 동일한 조건
        preorder_traversal(idx * 2)
        preorder_traversal(idx * 2 + 1)

# 중위 순회
def inorder_traversal(idx):
    # 부모 노드 차례가 중간인 순회 방식
    # 위의 함수를 순서만 바꿔보았더니 정상적으로 작동하지 않음
    # 어디까지 순회해야 하나?
    # 순회 대상이 범위 넘어가지 않도록
    if idx <= N:
        # left subtree에 대해서도 동일한 조건
        inorder_traversal(idx * 2)
        # 중위 순회는 왼쪽 서브트리를 순회 아후에 조사한다
        print(tree[idx], end=' ')
        inorder_traversal(idx * 2 + 1)


# 후위 순회
def postorder_traversal(idx):
    # 어디까지 순회해야 하나?
    # 순회 대상이 범위 넘어가지 않도록
    if idx <= N:
        # left subtree에 대해서도 동일한 조건
        postorder_traversal(idx * 2)
        postorder_traversal(idx * 2 + 1)
        print(tree[idx], end=' ')


N = 5
tree = [0, 'A', 'B', 'C', 'D', 'E']


'''
    트리 구조
        'A'
      /   \
   'B'    'C'
  /   \
'D'    'E'
'''

print('전위 순회')
# 트리를 결국 배열 형태로 만들 것
# 그 인덱스를 각 노드의 값이 삽입된 위치로 볼 것
# 루트노드에 해당하는 1번 인덱스부터 조회 시작
preorder_traversal(1)  # 'A' 'B' 'D' 'E' 'C'
print()
print('중위 순회')
inorder_traversal(1)  # 'D' 'B' 'E' 'A' 'C'
print()
print('후위 순회')
postorder_traversal(1)  # 'D' 'E' 'B' 'C''A'