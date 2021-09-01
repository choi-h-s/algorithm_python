
N, M = map(int, input().split())

x, y, d = map(int, input().split())

board = []

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

for _ in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)

result = 1
board[x][y] = 2

while True:
    d += 1
    if d >= 4:
        d = 0

    end = True

    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
            continue
        if board[next_x][next_y] == 0:
            end = False
            break

    if end:
        next_x = x - dx[d]
        next_y = y - dy[d]
        if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
            break

        if board[next_x][next_y] != 1:
            x = next_x
            y = next_y
            continue
        else:
            break

    next_x = x + dx[d]
    next_y = y + dy[d]
    if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
        continue

    if board[x + dx[d]][y+dy[d]] == 0:
        x = x + dx[d]
        y = y + dy[d]
        result += 1
        board[x][y] = 2
    else:
        continue

print(result)
