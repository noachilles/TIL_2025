class TreeNode:
    def __init__(self, key):
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드
        self.val = key  # 노드의 값

# 전위 순회
def preorder_traversal(root):
    if root:
        print(root.val)  # 현재 노드 방문
        preorder_traversal(root.left)  # 왼쪽 서브트리 방문
        preorder_traversal(root.right)  # 오른쪽 서브트리 방문

# 중위 순회
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)  # 왼쪽 서브트리 방문
        print(root.val)  # 현재 노드 방문
        inorder_traversal(root.right)  # 오른쪽 서브트리 방문

# 후위 순회
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)  # 왼쪽 서브트리 방문
        postorder_traversal(root.right)  # 오른쪽 서브트리 방문
        print(root.val)  # 현재 노드 방문

# 트리 생성
root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')

'''
    트리 구조
        'A'
      /   \
   'B'    'C'
  /   \
'D'    'E'
'''

print('전위 순회')
preorder_traversal(root)  # 'A' 'B' 'D' 'E' 'C'
print('중위 순회')
inorder_traversal(root)  # 'D' 'B' 'E' 'A' 'C'
print('후위 순회')
postorder_traversal(root)  # 'D' 'E' 'B' 'C''A'