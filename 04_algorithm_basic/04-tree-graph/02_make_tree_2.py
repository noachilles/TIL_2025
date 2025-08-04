# 부모의 정보만 주어질 때, 이진 트리 생성하기
# 자신의 값, 부모 인덱스 (부모가 0인 경우, 루트)
input_data = [
    ['A', 0],
    ['C', 1],
    ['B', 1],
    ['F', 3],
    ['G', 6],
    ['E', 2],
    ['D', 2]
]

N = 16
tree = [0] * (N+1)
print(tree)

for data in input_data:
    print(data)
    value = data[0]     # A
    parent = data[1]    # 0

    # 자식 idx 계산
    left_child = parent * 2
    right_child = parent * 2 + 1

    if not parent:
        tree[1] = value
        continue

    # 주어진 정보가 부모 노드의 idx뿐
    # 이진트리에서 어디에 삽입될 수 있는지 보려면
    # 부모 노드 왼, 오 자식 중 비어있는 곳 찾아야
    if not tree[left_child]:
        tree[left_child] = value
    else:
        tree[right_child] = value

print(tree)