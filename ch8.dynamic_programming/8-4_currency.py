
N, M = map(int, input().split())

money = []

for _ in range(N):
    money.append(int(input()))

result = [-1] * (M+1)

for i in range(1, M+1):
    if i in money:
        result[i] = 1
    else:
        for x in money:
            if i-x <= i or x > M:
                continue
            if result[i-x] != -1:
                if result[i] == -1:
                    result[i] = result[i-x] + 1
                else:
                    result[i] = min(result[i], result[i-x] + 1)

print(result)
print(result[M])