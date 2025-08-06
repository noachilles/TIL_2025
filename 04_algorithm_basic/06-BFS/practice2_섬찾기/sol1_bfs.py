import sys
sys.stdin = open('input.txt')


# 입력 처리
n, m = map(int, input().split())  # 지도의 크기
arr = [list(map(int, input())) for _ in range(n)]  # 지도 입력
island_cnt = 0  # 섬의 개수

