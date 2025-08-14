def perm(selected, remain):  
    '''
    Args:
        selected: 선택된 값 목록
        reamin: 선택되지 않고 남은 값 목록 
    '''
    # 모든 요소를 선택할 것 -> 나머지 없을 때까지
    # 뽑는 개수를 바꾸고 싶으면 remain이나 selected의 길이가 특정 길이일 때 종료하는 걸로 설정하면 됨
    if not remain:
        print(selected)
    else:
        for idx in range(len(remain)):
            # idx 번째의 요소를 선택
            select_item = remain[idx]
            # 선택된 idx번째를 제외한 remain을 만들자 (진짜 나머지 리스트)
            remain_list = remain[:idx] + remain[idx+1:]
            perm(selected + [select_item], remain_list)

# 초기 호출로 빈 리스트와 [1, 2, 3] 리스트 사용
perm([], [1, 2, 3])
