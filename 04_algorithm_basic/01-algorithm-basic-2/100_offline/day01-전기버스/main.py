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


def goby_bus(road, now, count, battery):
    # 만약 배터리가 없다면 돌아감
    if not battery:
        return

    for idx in range(now, N+1):
        if road[idx] == 0:
            goby_bus(road, now+1, count, battery-1)
        else:
            goby_bus(road, now+1, count+1, K)
            goby_bus(road, now+1, count, battery)

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    road = [0] * (N+1)
    chargers = list(map(int, input().split()))
    # chargers의 경로를 road에 저장함
    for idx in chargers:
        road[idx] = 1

