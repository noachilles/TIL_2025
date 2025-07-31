T = int(input())

def perm(arr, start_idx):
    # 모든 카드를 배열했다면 return
    global chk
    if start_idx == len(arr):
        # print(arr)
        if is_baby_gin(arr):
           chk = True
        return
    else:
        for idx in range(start_idx, len(arr)):
            arr[idx], arr[start_idx] = arr[start_idx], arr[idx]
            perm(arr, idx+1)
            arr[idx], arr[start_idx] = arr[start_idx], arr[idx]

def is_baby_gin(arr):
    # 앞의 3개가 run인지 확인
    run_a_chk = True
    run_d_chk = True
    # 앞의 3개가 triplet인지 확인
    triplet_chk = True
    for idx in range(2):
        if arr[idx+1] != arr[idx] + 1:
           run_a_chk = False
        if arr[idx+1] != arr[idx] - 1:
            run_d_chk = False
        if arr[idx+1] != arr[idx]:
            triplet_chk = False
    if not (run_a_chk or run_d_chk or triplet_chk):
        return False
    # 앞의 3개 통과시 - 뒤의 것 확인
    else:
        run_a_chk = True
        run_d_chk = True
        triplet_chk = True
        for idx in range(3, len(arr)-1):
            if arr[idx+1] != arr[idx] + 1:
                run_a_chk = False
            if arr[idx + 1] != arr[idx] - 1:
                run_d_chk = False
            if arr[idx+1] != arr[idx]:
                triplet_chk = False
        if not(run_a_chk or run_d_chk or triplet_chk):
            return False
    return True


# 순열 index 사용해서 한번 더 구현해보기

for tc in range(1, T+1):
    org = list(map(int, input().strip()))
    chk = False
    perm(org, 0)
    print(f'#{tc}', end=' ')
    if chk:
        print('true')
    else:
        print('false')