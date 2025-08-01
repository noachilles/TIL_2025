# 시간초과 발생
# def get_charger_list(arr, start_idx, num):
#     global chk_possible
#     if len(arr) == num:
#         # print(arr)
#         if bus_goby(arr):
#             chk_possible = True
#         return
#     else:
#         for idx in range(start_idx, len(chargers)):
#             get_charger_list(arr + [chargers[idx]], idx + 1, num)
#
# def bus_goby(arr):
#     now = 0
#     for idx in range(len(arr)):
#         if (arr[idx] - now) > K:
#             return False
#         now = arr[idx]
#     if (N - now) > K:
#         return False
#     return True
#
# T = int(input())
#
# for tc in range(1, T+1):
#     K, N, M = map(int, input().split())
#     chargers = list(map(int, input().split()))[:M]
#     res = 0
#     if chargers[-1] >= (N - K):
#         # 완전 탐색을 하려면 - 5개에 대한 모든 경우의 수를 생각한다
#         for num in range(1, N):
#             chk_possible = False
#             get_charger_list([], 0, num)
#             if chk_possible:
#                 res = num
#                 break
#
#     print(f'#{tc}', end=' ')
#     print(res)
#

# 시간초과 발생
def goby_bus(road, now, count, battery):
    global res

    # 만약 배터리가 없다면 돌아감
    if battery < 0 or res <= M:
        return

    # 배터리가 모두 닳지 않았으며 현재 위치가 종점이라면
    if now == N:
        if res > count:
            res = count
        return

    # 만약 현재 위치에 충전소가 없다면
    if road[now] == 0:
        # 앞으로 전진만 할 수 있음
        goby_bus(road, now+1, count, battery-1)
    # 만약 현재 위치에 충전소가 있다면
    else:
        # 앞으로 전진
        goby_bus(road, now+1, count, battery-1)
        # 충전 후 전진
        goby_bus(road, now+1, count+1, K-1)

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    road = [0] * (N+1)
    chargers = list(map(int, input().split()))
    # chargers의 경로를 road에 저장함
    for idx in chargers:
        road[idx] = 1
    res = M + 1
    goby_bus(road, 0, 0, K)
    
    print(f'#{tc}', end=' ')
    if res > M:
        print(0)
    else:
        print(res)
