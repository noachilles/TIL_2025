def hanoi(n, source, auxiliary, target):
    """
    n개의 원반을 source 기둥에서 target 기둥으로 옮깁니다.

    Args:
        n (int): 이동할 원반의 개수
        source (str): 시작 기둥 (예: 'A')
        auxiliary (str): 보조 기둥 (예: 'B')
        target (str): 목표 기둥 (예: 'C')
    """
    # 일단, 옮겨야 할 원판의 수가 1개보단 많아야 일을 한다.
    if n > 0:
        # 1단계: 가장 큰 원반을 옮기기 위한 준비
        # n-1 개의 원반들을 모두 옮겨야 함 -> 보조 기둥으로
        hanoi(n-1, source, target, auxiliary) # n-1개의 원판(가장 큰 X) auxiliary가 목표이고, target 기둥을 보조로 사용함

        print(f'원반 {n}을 {source}에서 {target}으로 이동하였음.')

        # 3단계: 마무리 작업
        # 가장 큰 원반을 옮기는 데 성공했으니
        # 보조 기둥 (각각의 원반 기준으로 보조기둥)에서 다시 target 기둥으로 옮기기
        hanoi(n-1, auxiliary, source, target)

# --- 실행 예시 ---
# 3개의 원반을 'A' 기둥에서 'C' 기둥으로 옮기기 ('B' 기둥을 보조로 사용)
number_of_disks = 3
hanoi(number_of_disks, 'A', 'B', 'C')