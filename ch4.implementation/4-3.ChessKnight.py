
x = ["a", "b", "c", "d", "e", "f", "g", "h"]
y = ["1", "2", "3", "4", "5", "6", "7", "8"]

dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [1, -1, 1, -1, +2, -2, +2, -2]

knight = input()

knight_x = x.index(knight[0])
knight_y = y.index(knight[1])

result = 0
for i in range(len(dx)):
    tmp_x = knight_x + dx[i]
    tmp_y = knight_y + dy[i]

    if tmp_x < 0 or tmp_x >= 8 or tmp_y < 0 or tmp_y >= 8:
        pass
    else:
        result += 1

print(result)