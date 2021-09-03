"""


"""

N, K = map(int, input().split())

first = list(map(int, input().split()))
second = list(map(int, input().split()))

first.sort()
second.sort(reverse=True)

i = j = 0

while K > 0:
    if i >= len(first) or j >= len(second):
        break

    if first[i] < second[j]:
        first[i], second[j] = second[j], first[i]
        K -= 1
        i += 1
        j += 1
    elif first[i] > second[j]:
        i += 1
        j += 1
    else:
        i += 1

print(sum(first))
