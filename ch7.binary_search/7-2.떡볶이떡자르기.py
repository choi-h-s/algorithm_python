import sys

input_num = sys.stdin.readline().rstrip()
N, M = map(int, input_num.split())

ricecakes = list(map(int, input().split()))

start = 0
end = max(ricecakes)

result = 0

while start <= end:
    total = 0

    mid = (start + end) // 2

    for ricecake in ricecakes:
        if ricecake > mid:
            total += ricecake - mid

    if total >= M:
        result = max(result, mid)
        start = mid + 1
    else:
        end = mid - 1

print(result)
