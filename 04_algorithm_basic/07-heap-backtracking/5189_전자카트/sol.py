import sys
sys.stdin = open('input.txt')

def get_min_battery_consume(idx, consume_sum):
    '''
    idx: 현재 카트의 위치
    battery_consume: 여태까지 배터리 소모량의 합
    :return:
    '''
    global min_consume
    # 가지치기 진행 - 만약 이전 값보다 크다면 아래로 방문하지 않음
    if consume_sum >= min_consume:
        return

    # 만약 모든 관리 장소를 돌아서, 사무실만 방문하지 않았다면
    if visited.count(0) == 1:
        # 사무실로 돌아가는 배터리 소모량을 더해서 min값과 비교
        consume_sum += grid[idx][0]
        if consume_sum < min_consume:
            min_consume = consume_sum
        return
    # 현재 위치에서 갈 수 있는 모든 경로를 탐색함: 이미 방문한 곳 제외 / 사무실 (0 index) 제외
    for nxt in range(1, N):
        if visited[nxt]:
            continue
        else:
            visited[nxt] = 1
            get_min_battery_consume(nxt, consume_sum + grid[idx][nxt])
            # 방문 기록을 초기화 - 다른 경로를 찾을 수 있도록
            visited[nxt] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    # 방문 확인을 위한 list
    visited = [0] * N

    # 1번으로 돌아오는 데까지 걸리는 최소 배터리 사용량
    min_consume = 10001
    # 함수 호출 횟수 구해보기
    # cnt = 0
    # 1번에서 출발해 최소 배터리 사용량 출력
    get_min_battery_consume(0, 0)
    # N=10일 때, 987410 -> 14486까지 줄일 수 있었음
    # print(min_consume, cnt) # 89 5 / 96 16 / 139 65
    print(f'#{tc} {min_consume}')