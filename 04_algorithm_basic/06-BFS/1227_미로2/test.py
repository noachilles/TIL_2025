from collections import deque

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(maze, start):
    visited = [[0] * 100 for _ in range(100)]
    queue = deque([start])
    visited[start[0]][start[1]] = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in direction:
            nx, ny = dx + x, dy + y
            if 0 <= nx < 100 and 0 <= ny < 100:
                if maze[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                elif maze[nx][ny] == 3:
                    return 1

    return 0


for _ in range(1, 11):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(100)]

    maze = [[int(d) for d in str(num[0])] for num in data]

    found_s = False

    start = None
    dst = None

    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                start = [i, j]
                found_s = True
                break
        if found_s == 1:
            break

    result = bfs(maze, start)
    print(f"#{N} {result}")