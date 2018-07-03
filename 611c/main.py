from sys import stdin, stdout
# import time

def transpose(matrix):
    temp = list(zip(*matrix))
    for i in range(len(temp)):
        temp[i] = ''.join(temp[i])
    return temp

height, width = map(int, stdin.readline().rstrip().split())
board = [None] * height
for i in range(height):
    board[i] = stdin.readline().rstrip()

requests = int(stdin.readline().rstrip())
areas = [None] * requests
for i in range(requests):
    areas[i] = list(map(int, stdin.readline().rstrip().split()))

# start_time = time.time()
hboard = board
vboard = transpose(board)
for area in areas:
    placings = 0
    for i in range(area[0] - 1, area[2]):
        row = hboard[i][area[1] - 1:area[3]]
        clean_parts = list(filter(None, row.split('#')))
        placings += len(''.join(clean_parts)) - len(clean_parts)
    for i in range(area[1] - 1, area[3]):
        col = vboard[i][area[0] - 1:area[2]]
        clean_parts = list(filter(None, col.split('#')))
        placings += len(''.join(clean_parts)) - len(clean_parts)
    stdout.write(str(placings) + "\n")

# stdout.write("finished in: {0}\n".format(time.time() - start_time))
