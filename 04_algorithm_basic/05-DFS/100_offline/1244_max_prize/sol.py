import sys
sys.stdin = open('input.txt')

def depth_first_search(number, cnt):
    global max_value
    # 만약 동일한 횟수에 같은 값을 갖는 배열을 순회한 경험이 있다면 - 그 아래까지 다녀온 것
    if ''.join(number) + str(cnt) in checked:
        return
    # 방문한 적이 없디면 방문 처리한다.
    checked.add(''.join(number) + str(cnt))
    # 만약 횟수가 모두 채워졌다면
    if cnt == M:
        value = int(''.join(number))
        if max_value < value:
            max_value = value
        return

    # 첫번째 인덱스
    for i in range(len(number)-1):
        # 두번째 인덱스
        for j in range(i+1, len(number)):
            # 서로 자리를 바꿈
            number[i], number[j] = number[j], number[i]
            depth_first_search(number, cnt + 1)
            # 원상 복귀
            number[i], number[j] = number[j], number[i]

T = int(input())
for tc in range(1, T+1):
    # max값과 이미 확인한 값을 넣을 set을 선언
    max_value = -1000000
    checked = set()
    # input
    input_data = input().split()
    # N: 숫자로 이루어진 문자열(배열로 사용), M: 교환해야 하는 횟수
    N, M = list(input_data[0]), int(input_data[1])
    depth_first_search(N, 0)
    print(f'#{tc} {max_value}')