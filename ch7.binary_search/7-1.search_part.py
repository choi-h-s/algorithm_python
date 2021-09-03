import sys

N = sys.stdin.readline().rstrip()
N = int(N)
store_parts = sys.stdin.readline().rstrip()
store_parts = list(map(int, store_parts.split()))
store_parts.sort()

M = sys.stdin.readline().rstrip()
M = int(M)
customer_parts = sys.stdin.readline().rstrip()
customer_parts = list(map(int, customer_parts.split()))


def binary_search(target, array: list, start: int, end: int) -> int:

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


for customer_part in customer_parts:
    result = binary_search(customer_part, store_parts, 0, N-1)
    if result != -1:
        print("yes", end=" ")
    else:
        print("no", end=" ")

