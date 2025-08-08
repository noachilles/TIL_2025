import sys
sys.stdin = open("input.txt")

from collections import deque

# 상하좌우 방향벡터 (상:0, 하:1, 좌:2, 우:3)
direction_vectors = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def simulate_with_bfs():
    """
    BFS를 사용한 원자 소멸 시뮬레이션
    
    **시간초과 발생 원인:**
    1. 매 시간마다 큐의 모든 원소를 순회하면서 충돌 검사 (O(N²))
    2. 불필요한 좌표 변환으로 인한 복잡성 증가
    3. 2차원 필드 배열 생성으로 메모리 사용량 증가
    4. BFS 특성상 매 스텝마다 큐를 재구성하는 오버헤드
    5. 충돌 검사 로직이 비효율적 (선형 탐색)
    
    **개선 방안:**
    1.
    2.
    3.
    """
    global simulation_result, min_y_coord, min_x_coord, max_y_coord, max_x_coord
    
    while atom_queue:
        current_x, current_y, direction, energy = atom_queue.popleft()
        
        # 다음 위치 계산
        next_x = current_x + direction_vectors[direction][0]
        next_y = current_y + direction_vectors[direction][1]
        
        # 경계 체크 (비효율적인 범위 설정)
        if min_x_coord - 1 <= next_x <= max_x_coord + 1 and min_x_coord - 1 <= next_y <= max_x_coord + 1:
            # 충돌 검사 - O(N) 시간복잡도로 매우 비효율적
            collision_found = False
            for queue_index in range(len(atom_queue)):
                other_atom = atom_queue[queue_index]
                other_next_x = other_atom[0] + direction_vectors[other_atom[2]][0]
                other_next_y = other_atom[1] + direction_vectors[other_atom[2]][1]
                
                # 충돌 조건 검사
                if (next_x == other_next_x and next_y == other_next_y and 
                    current_x == other_next_x and current_y == other_next_y):
                    simulation_result += other_atom[3] + energy
                    collision_found = True
                    break
            
            if not collision_found:
                atom_queue.append([next_x, next_y, direction, energy])

# 테스트 케이스 처리
test_case_count = int(input())
for test_case in range(1, test_case_count + 1):
    atom_count = int(input())
    atom_data = [list(map(int, input().split())) for _ in range(atom_count)]
    simulation_result = 0
    
    # BFS를 위한 큐 초기화
    atom_queue = deque()
    for atom_info in atom_data:
        atom_queue.append(atom_info)
    
    # 최소 좌표 찾기 (비효율적인 방법)
    min_x_coord = 987654321
    min_y_coord = 987654321
    for atom_info in atom_data:
        if min_x_coord >= atom_info[0]:
            min_x_coord = atom_info[0]
        if min_y_coord >= atom_info[1]:
            min_y_coord = atom_info[1]
    
    # 좌표 이동 (불필요한 좌표 변환)
    for atom_info in atom_data:
        atom_info[0] += abs(min_x_coord)
        atom_info[1] += abs(min_y_coord)
    
    # 최대 좌표 찾기
    max_x_coord = -2000
    max_y_coord = -2000
    for atom_info in atom_data:
        if max_x_coord <= atom_info[0]:
            max_x_coord = atom_info[0]
        if max_y_coord <= atom_info[1]:
            max_y_coord = atom_info[1]
    
    # 불필요한 2차원 필드 배열 생성 (메모리 낭비)
    simulation_field = [[0] * (max_x_coord + 1) for _ in range(max_y_coord + 1)]
    for atom_info in atom_data:
        simulation_field[atom_info[1]][atom_info[0]] = atom_info[3]
    
    # 시뮬레이션 실행
    simulate_with_bfs()
    
    print(f"#{test_case} {simulation_result}")
