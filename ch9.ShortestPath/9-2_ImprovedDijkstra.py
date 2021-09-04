import heapq
import sys

INF = 10e+9

N, M = map(int, input().split())

start = int(input())

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    x, y, cost = map(int, input().split())

    graph[x].append((y, cost))


def dijkstra(start):

    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = q.pop()

        if distance[node] < dist:
            continue

        for next_node, weight in graph[node]:
            next_dist = dist + weight
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heapq.heappush(q, (next_dist, next_node))


dijkstra(start)

for i in range(1, N+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
