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


# def goby_bus(road, now, count, battery):
#     global res
#     # 만약 현재 위치가 종점이라면
#     if now == N:
#         if res > count:
#             res = count
#         return
#     # 만약 배터리가 없다면 돌아간다.
#     if battery < 0:
#         return

#     # 해당 위치에 충전소가 없다면
#     if road[now] == 0:
#         # battery는 1 줄고, 현재 위치는 한 칸 전진
#         goby_bus(road, now+1, count, battery-1)
#     # 아닐 경우
#     else:
#         # battery를 충전했을 때: K-1을 배터리 값으로 설정하고 한 칸 전진
#         goby_bus(road, now+1, count+1, K-1)
#         # 배터리를 충전하지 않았을 때: 현재 배터리애서 1 빼고 한 칸 전진
#         goby_bus(road, now+1, count, battery-1)

# T = int(input())

# for tc in range(1, T+1):
#     K, N, M = map(int, input().split())
#     road = [0] * (N+1)
#     chargers = list(map(int, input().split()))
#     # chargers의 경로를 road에 저장함
#     for idx in chargers:
#         road[idx] = 1

#     res = M+1
#     goby_bus(road, 0, 0, K)
#     print(f'#{tc}', end=' ')
#     if res > M:
#         print(0)
#     else:
#         print(res)

def goby_bus():
    # 가장 가까운 충전소 저장
    nearest = 0
    # 충전 횟수
    cnt = 0
    # 현재 위치
    now = 0
    battery = K
    # 길의 모든 칸을 돌면서 한 칸씩 전진한다.
    # 현재 위치가 N이 되면 종료  
    while now != N:
        now += 1
        battery -= 1
        print(now, battery)
        if road[now] == 1:
            nearest = now
        # 만약 배터리가 없다면
        if battery < 0:
            if road[nearest] == 2:
                return False
            else:
                now = nearest
                battery = K
                cnt += 1
                road[nearest] = 2
    return cnt
            

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    
    road = [0] * (N+1)
    