"""
    N * M size의 얼음틀 구멍은 0 , 칸막이는 1

"""


def dfs(x, y):
    global frame

    if x < 0 or x >= N:
        return 0
    if y < 0 or y >= M:
        return 0

    if frame[x][y] == 1:
        return 0

    frame[x][y] = 1

    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y+1)
    dfs(x, y-1)

    return 1


N, M = map(int, input().split())

frame = []

for i in range(N):
    frame.append(list(map(int, input())))

result = 0

for i in range(N):
    for j in range(M):
        result += dfs(i, j)

print(result)
