"""
    이것이 취업을 위한 코딩테스트다
    3-1. 큰 수의 법칙
    수학적으로 계산

    max number K 개, second number 1개 , max number K개, second max 1개 , ...
"""

N, M, K = map(int, input().split())

numbers = list(map(int, input().split()))
numbers = sorted(numbers, reverse=True)

first = numbers[0]
second = numbers[1]

result = 0

first_count = M // (K+1) * K + M % (K+1)
second_count = M - first_count

result = first * first_count + second * second_count

print(result)
