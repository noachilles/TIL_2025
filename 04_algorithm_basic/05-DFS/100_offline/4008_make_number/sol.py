import sys
sys.stdin = open('input.txt')

def operating(total, next, idx):
    '''
        total: 기존에 연산된 값
        next: 다음 연산 대상
        idx: 연산자 index
        return: next를 대상으로 total을 연산한 결과
    '''
    if idx == 0:
        return total + next
    elif idx == 1:
        return total - next
    elif idx == 2:
        return total * next
    else:
        return int(total/next)

def depth_first_search(arr, now, total):
    '''
        arr: 연산자 개수 정보가 담긴 배열
        now: 다음 연산 대상이 되는 수를 가리키는 숫자 인덱스(1부터 시작)
        total: 지금까지의 연산결과(배열 index 0부터 시작)
    '''
    global min_value, max_value
    # 만약 모든 연산자를 다 사용했다면:
    if now == len(numbers):
        min_value = min(min_value, total)
        max_value = max(max_value, total)
        return
    # 아직 남은 연산자가 있을 경우에는:
    else:
        next = now + 1
        for idx in range(len(arr)):
            # arr[idx]가 0보다 크다면 = 연산자가 아직 남아있다면
            if arr[idx] > 0:
                # 사용 처리를 하고
                arr[idx] -= 1
                # 현재 값에 해당 idx 연산을 수행함
                new_total = operating(total, numbers[now], idx) # 현재 연산값, 다음 값, 연산자 idx
                # 연산 결과를 반영해 재귀
                depth_first_search(arr, next, new_total) # 연산 결과를 넘겨줌
                # 원상 복귀
                arr[idx] += 1


T = int(input())
for tc in range(1, T+1):
    min_value = 100000001
    max_value = -100000001
    N = int(input())
    operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    # 초깃값 설정: 연산자 개수가 담긴 배열, 다음 연산을 수행할 숫자 인덱스, 최초 인덱스값
    depth_first_search(operators, 1, numbers[0])
    print(f'#{tc} {max_value - min_value}')
