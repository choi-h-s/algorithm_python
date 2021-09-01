from collections import deque


def bfs():
    global maze
    global N, M
    queue = deque()

    queue.append((0, 0, 0))
    maze[0][0] =1

    result = 40000

    while queue:
        x, y, count = queue.popleft()

        count += 1

        if x == N-1 and y == M-1:
            result = min(count, result)
            continue

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(len(dx)):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                continue
            if maze[next_x][next_y] == 1:
                maze[next_x][next_y] = maze[x][y] + 1
                queue.append((next_x, next_y, count))

    return result


N, M = map(int, input().split())

maze = []

for _ in range(N):
    maze.append(list(map(int, input())))

print(bfs())
