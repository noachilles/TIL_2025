class TreeNode:
    def __init__(self, value):
        self.value = value  # 노드의 값을 저장
        self.left = None    # 왼쪽 자식 노드를 가리키는 포인터
        self.right = None   # 오른쪽 자식 노드를 가리키는 포인터

class BinaryTree:
    def __init__(self):
        self.root = None  # 루트 노드 초기화
    
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)  # 트리가 비어 있으면 루트 노드로 설정
        else:
            self._insert_recursive(self.root, value)  # 루트 노드부터 재귀적으로 삽입
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)  # 왼쪽 자식이 없으면 왼쪽에 삽입
            else:
                self._insert_recursive(node.left, value)  # 왼쪽 자식이 있으면 재귀적으로 왼쪽에 삽입
        else:
            if node.right is None:
                node.right = TreeNode(value)  # 오른쪽 자식이 없으면 오른쪽에 삽입
            else:
                self._insert_recursive(node.right, value)  # 오른쪽 자식이 있으면 재귀적으로 오른쪽에 삽입
    
    def search(self, value):
        return self._search_recursive(self.root, value)  # 루트 노드부터 재귀적으로 검색
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node  # 노드가 없거나 값을 찾으면 해당 노드를 반환
        if value < node.value:
            return self._search_recursive(node.left, value)  # 왼쪽 자식에서 재귀적으로 검색
        else:
            return self._search_recursive(node.right, value)  # 오른쪽 자식에서 재귀적으로 검색
    
    def inorder_traversal(self):
        nodes = []
        self._inorder_recursive(self.root, nodes)  # 중위 순회 시작
        return nodes
    
    def _inorder_recursive(self, node, nodes):
        if node:
            self._inorder_recursive(node.left, nodes)  # 왼쪽 자식을 중위 순회
            nodes.append(node.value)  # 현재 노드의 값을 추가
            self._inorder_recursive(node.right, nodes)  # 오른쪽 자식을 중위 순회
    
    def __str__(self):
        return str(self.inorder_traversal())

# 이진 트리 생성 및 값 삽입
bt = BinaryTree()
bt.insert('A')
bt.insert('B')
bt.insert('C')
bt.insert('D')
bt.insert('E')
bt.insert('F')
bt.insert('G')
bt.insert('H')
bt.insert('I')
bt.insert('J')
bt.insert('K')
bt.insert('L')

# 이진 트리 출력
print("Binary Tree (Inorder Traversal):", bt)

# 노드 검색
print("Search for node with value 'E':", bt.search('E')) 
print("Search for node with value 'E':", bt.search('E').value)  
print("Search for node with value 'Z':", bt.search('Z')) 
