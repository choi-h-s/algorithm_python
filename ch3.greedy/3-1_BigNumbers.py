"""
    이것이 취업을 위한 코딩테스트다
    3-1. 큰 수의 법칙
    반복방식
"""
N, M, K = map(int, input().split())

numbers = list(map(int, input().split()))
numbers = sorted(numbers, reverse=True)

result = 0

while M > 0:
    if M >= K:
        M -= K
        result += K * numbers[0]

        if M > 0:
            M -= 1
            result += numbers[1]

    else:
        result += M * numbers[0]
        M = 0

print(result)
