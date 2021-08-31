"""
    카드 게임

    N * M 의 카드 중
    각 행의 최소인 값들을 뽑는 카드게임에서
    얻을 수 있는 최대 값을 출력하라
"""
N, M = map(int, input().split())

result = 0

for i in range(N):
    numbers = list(map(int, input().split()))

    min_value = min(numbers)

    result = max(result, min_value)

print(result)