from sys import stdin, stdout
import random

height, width = map(int, stdin.readline().rstrip().split())
board = [['.'] * width for i in range(height)]

for row in board:
    step = random.randint(2, 5)
    first = random.randint(0, 4)
    for i in range(first, len(row), step):
        row[i] = '#'

for row in board:
    for val in row:
        stdout.write(str(val))
    stdout.write("\n")

requests = int(stdin.readline().rstrip())
areas = [None] * requests
for i in range(requests):
    y2 = random.randint(1, height)
    x2 = random.randint(1, width)
    y1 = random.randint(1, y2)
    x1 = random.randint(1, x2)
    areas[i] = [y1, x1, y2, x2]


for row in areas:
    stdout.write(' '.join(map(str, row)))
    stdout.write("\n")