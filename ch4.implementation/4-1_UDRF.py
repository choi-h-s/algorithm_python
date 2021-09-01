
N = int(input())

directions = list(input().split())

x, y = 1, 1

for direction in directions:
    if direction == "D":
        x += 1
        if x > N:
            x = N

    elif direction == "U":
        x -= 1
        if x <= 0:
            x = 1
    elif direction == "L":
        y -= 1
        if y <= 0:
            y = 1
    elif direction == "R":
        y += 1
        if y >= N:
            y = N

print("{} {}".format(x, y))
