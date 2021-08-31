"""
    1이 될때까지
    어떠한 수 N이 1이 될 때까지 반복적으로 수행
    1. N - 1
    2. N // K

    N, K는 2 이상 100,000이하의 자연수
    이 횟수가 최소가 될때 몇 회 인지 구하라.
"""

N, K = map(int, input().split())

result = 0

while N > 1:
    if N % K == 0:
        N //= K
    else:
        N -= 1

    result += 1

print(result)
