
N = int(input())

result = 0

for i in range(N+1):
    if i % 10 == 3:
        result += 3600
    else:
        for j in range(60):
            if j // 10 == 3 or j % 10 == 3:
                result += 60
            else:
                result += len([x for x in range(60) if x // 10 == 3 or x % 10 == 3])

print(result)
