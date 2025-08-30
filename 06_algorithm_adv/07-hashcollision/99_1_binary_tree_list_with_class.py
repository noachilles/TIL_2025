class BinaryTree:
    def __init__(self):
        # 이진 트리를 저장할 리스트
        self.tree = ['A', 'B', 'C', 'D', 'E',
                     'F', 'G', 'H', 'I', 'J', 'K', 'L']
    
    def insert(self, value):
        # 리스트 끝에 값을 추가하여 트리에 삽입
        self.tree.append(value)

    def get_node(self, index):
        # 주어진 인덱스의 노드를 반환, 인덱스가 유효하지 않으면 None 반환
        if index < len(self.tree):
            return self.tree[index]
        return None

    def set_node(self, index, value):
        # 주어진 인덱스에 노드 값을 설정
        # 만약 인덱스가 현재 리스트의 범위를 벗어나면 리스트를 확장
        while len(self.tree) <= index:
            self.tree.append(None)
        self.tree[index] = value
    
    def get_left_child(self, index):
        # 주어진 인덱스의 왼쪽 자식 인덱스 계산
        left_index = 2 * index + 1
        # 왼쪽 자식이 리스트 범위 내에 있으면 해당 값을 반환
        if left_index < len(self.tree):
            return self.tree[left_index]
        return None
    
    def get_right_child(self, index):
        # 주어진 인덱스의 오른쪽 자식 인덱스 계산
        right_index = 2 * index + 2
        # 오른쪽 자식이 리스트 범위 내에 있으면 해당 값을 반환
        if right_index < len(self.tree):
            return self.tree[right_index]
        return None
    
    def get_parent(self, index):
        # 루트 노드는 부모가 없으므로 None 반환
        if index == 0:
            return None
        # 주어진 인덱스의 부모 인덱스 계산
        parent_index = (index - 1) // 2
        return self.tree[parent_index]
    
    def __str__(self):
        return str(self.tree)

# 이진 트리 생성
bt = BinaryTree()
bt.insert('M')

# 이진 트리 출력 
print("Binary Tree:", bt)
# 루트 노드 반환
print('루트노드:', bt.get_node(0))
# 'B', 'C' 의 부모 노드 반환 
print('B의 부모노드:', bt.get_parent(1))
print('C의 부모노드:', bt.get_parent(2))
# 루트 노드의 왼쪽 자식 B 출력
print('루트노드 왼쪽자식:', bt.get_left_child(0))  
# 루트 노드의 오른쪽 자식 C 출력
print('루트노드 오른쪽자식:', bt.get_right_child(0)) 
