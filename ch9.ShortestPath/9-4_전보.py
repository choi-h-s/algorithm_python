import heapq
import sys

N, M, C = map(int, input().split())

graph = [[] for _ in range(N+1)]
INF = int(1e+10)
weights = [INF] * (N+1)

for _ in range(M):
    x = sys.stdin.readline().rstrip()
    x, y, cost = map(int, x.split())
    graph[x].append((y, cost))


def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))

    while q:
        cur_weight, cur_node = heapq.heappop(q)

        if cur_weight >= weights[cur_node]:
            continue

        for next_node, next_weight in graph[cur_node]:
            if cur_weight + next_weight < weights[next_node]:
                weights[next_node] = cur_weight + next_weight
                heapq.heappush(q, (weights[next_node], next_node))


dijkstra(C)

count = 0
time = 0

for x in weights:
    if x < INF:
        count += 1
        time = max(time, x)

print(count, time)
