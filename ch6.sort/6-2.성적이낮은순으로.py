"""


"""

N = int(input())

grades = []

for _ in range(N):
    name, grade = input().split()
    grade = int(grade)

    grades.append((name, grade))

grades.sort(key=lambda x: x[1])

for grade in grades:
    print(grade[0], end=" ")
