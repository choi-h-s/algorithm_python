INF = int(1e+9)

n = int(input())
m = int(input())

board = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    board[i][i] = 0

for _ in range(m):
    x, y, cost = map(int, input().split())
    board[x][y] = cost

for i in range(1, n+1):

    for j in range(1, n+1):
        if i == j:
            continue

        for k in range(1, n+1):
            if k == j or k == i:
                continue
            board[j][k] = min(board[j][k], board[j][i] + board[i][k])


for x in range(1,n+1):
    for y in range(1, n+1):
        if board[x][y] == INF:
            print(INF, end=" ")
        else:
            print(board[x][y], end=" ")
    print()
