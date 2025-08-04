class Node:
    def __init__(self, key):
        self.key = key  # 노드의 값
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드

class BST:
    def __init__(self):
        self.root = None  # 루트 노드를 초기화

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)  # 트리가 비어 있으면 루트 노드로 설정
        else:
            self._insert(self.root, key)  # 재귀적으로 삽입

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)  # 왼쪽 자식이 없으면 왼쪽에 삽입
            else:
                self._insert(node.left, key)  # 왼쪽 자식이 있으면 재귀적으로 삽입
        else:
            if node.right is None:
                node.right = Node(key)  # 오른쪽 자식이 없으면 오른쪽에 삽입
            else:
                self._insert(node.right, key)  # 오른쪽 자식이 있으면 재귀적으로 삽입

    def delete(self, key):
        self.root = self._delete(self.root, key)  # 루트 노드부터 재귀적으로 삭제

    def _delete(self, node, key):
        if node is None:
            return node  # 노드가 없으면 그대로 반환

        if key < node.key:
            node.left = self._delete(node.left, key)  # 왼쪽 서브트리에서 삭제
        elif key > node.key:
            node.right = self._delete(node.right, key)  # 오른쪽 서브트리에서 삭제
        else:
            if node.left is None:
                return node.right  # 왼쪽 자식이 없으면 오른쪽 자식을 반환
            elif node.right is None:
                return node.left  # 오른쪽 자식이 없으면 왼쪽 자식을 반환

            temp = self._minValueNode(node.right)  # 오른쪽 서브트리의 최소값 노드를 찾음
            node.key = temp.key  # 현재 노드의 키를 최소값 노드의 키로 대체
            node.right = self._delete(node.right, temp.key)  # 최소값 노드를 삭제

        return node

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left  # 왼쪽 자식이 없을 때까지 이동하여 최소값 노드를 찾음
        return current

    def search(self, key):
        return self._search(self.root, key)  # 루트 노드부터 재귀적으로 검색

    def _search(self, node, key):
        if node is None or node.key == key:
            return node  # 노드가 없거나 값을 찾으면 해당 노드를 반환
        if key < node.key:
            return self._search(node.left, key)  # 왼쪽 서브트리에서 검색
        return self._search(node.right, key)  # 오른쪽 서브트리에서 검색

    def inorder(self):
        self._inorder(self.root)  # 중위 순회 시작
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)  
            print(node.key, end=' ') 
            self._inorder(node.right) 

# BST 생성
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)

bst.inorder()
