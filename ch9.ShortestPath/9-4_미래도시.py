INF = int(1e+10)

N, M = map(int, input().split())

graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

X, K = map(int, input().split())

for i in range(N+1):
    for j in range(N+1):
        for k in range(N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = graph[1][K] + graph[K][X]
if result >= INF:
    print(-1)
else:
    print(result)
