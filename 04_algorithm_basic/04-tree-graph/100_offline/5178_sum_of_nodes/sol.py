import sys
sys.stdin = open('input.txt')

def set_sums():
    for idx in range(len(graph)-1, 0, -1):
        parent, direction = divmod(idx, 2)
        if 0 < parent <= N and not graph[parent]:
            if direction == 0:
                graph[parent] = graph[idx] + (graph[idx+1] if idx+1 <= N else 0)
            else:
                graph[parent] = graph[idx] + graph[idx-1]


T = int(input())

for tc in range(1, T+1):

    N, M, L = map(int, input().split()) # 노드 개수 , 리프 노드 개수 , 출력할 노드 번호
    graph = [0] * (N+1)
    for i in range(M):
        idx, value = map(int, input().split())
        graph[idx] = value

    set_sums()
    print(f'#{tc}', end=' ')
    print(graph[L])

# 발표
## 조사 대상을 L 이상의 index로 한정지을 수 있음
## binary tree를 구현하는 방식이 class일 때, 오히려 로직이 더 복잡해질 수 있음